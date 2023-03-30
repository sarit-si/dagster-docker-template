from dagster import asset, MetadataValue, Output

@asset
def hello(context):

    message = "Hello World!!!"

    context.log.info(message)

    metadata = {
        "Message": MetadataValue.md(message)
    }

    return Output(value=message, metadata=metadata)
