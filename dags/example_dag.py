from dagster import asset, MetadataValue, Output

@asset
def gen_message():
    return "Hi User"

@asset
def show_message(context, gen_message):

    context.log.info(gen_message)

    metadata = {
        "Message": MetadataValue.md(gen_message)
    }

    return Output(value=gen_message, metadata=metadata)
