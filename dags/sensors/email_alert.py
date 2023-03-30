from dagster import (
    run_status_sensor,
    run_failure_sensor,
    RunFailureSensorContext,
    DagsterRunStatus,
    build_init_resource_context
)
from resources import customer_success_email

@run_status_sensor(
    run_status=DagsterRunStatus.SUCCESS,
    monitor_all_repositories=True
) # type: ignore
def send_success_email(context):

    resource_context = build_init_resource_context(
        config={
            "username": {"env" : "EMAIL_CUSTOMER_SUCCESS_USERNAME"},
            "password": {"env" : "EMAIL_CUSTOMER_SUCCESS_PASSWORD"},
            "subject": f"JOB SUCCESS ALERT",
            "message": f"job name: {context.dagster_run.job_name}"
        }
    )

    customer_success_email.email_sender(resource_context)

@run_failure_sensor(
    monitor_all_repositories=True
) # type: ignore
def send_failure_email(context: RunFailureSensorContext):

    resource_context = build_init_resource_context(
        config={
            "username": {"env" : "EMAIL_CUSTOMER_SUCCESS_USERNAME"},
            "password": {"env" : "EMAIL_CUSTOMER_SUCCESS_PASSWORD"},
            "subject": f"JOB FAILURE ALERT",
            "message": f"job name: {context.dagster_run.job_name}"
        }
    )

    customer_success_email.email_sender(resource_context)