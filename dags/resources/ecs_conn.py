import boto3
from dagster import resource, StringSource

class ECS:

    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, region_name: str):

        self.client = boto3.client('ecs',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name

        )

    def run(self, command: list, cluster: str, container_name: str, task_definition: str, subnets: list, launch_type: str='FARGATE') -> dict:

        return self.client.run_task(
            cluster=cluster,
            taskDefinition=task_definition,
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': subnets,
                    'assignPublicIp': 'ENABLED',
                }
            },
            launchType=launch_type,
            overrides={
                "containerOverrides": [
                    {
                        "name": container_name,
                        "command": command,
                    },
                ],
            },
        )

    def status(self, task_arn, cluster) -> str:

        return self.client.describe_tasks(
            cluster=cluster,
            tasks=[task_arn]
        )['tasks'][0]['lastStatus']

    def close(self):
        self.client.close()


@resource(
    config_schema={
        "aws_access_key_id": StringSource,
        "aws_secret_access_key": StringSource,
        "region_name": StringSource
    }
)
def ecs_instance(init_context):

    aws_access_key_id = init_context.resource_config["aws_access_key_id"]
    aws_secret_access_key = init_context.resource_config["aws_secret_access_key"]
    region_name = init_context.resource_config["region_name"]

    client = ECS(aws_access_key_id, aws_secret_access_key, region_name)

    return client


