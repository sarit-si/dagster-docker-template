from sqlalchemy import create_engine
from dagster import resource, StringSource

@resource(
    config_schema={
        "host": StringSource,
        "username": StringSource,
        "password": StringSource,
        "port": StringSource
    } # type: ignore
)
def scraper_db(init_context):

    HOST = init_context.resource_config["host"]
    USERNAME = init_context.resource_config["username"]
    PASSWORD = init_context.resource_config["password"]
    PORT = init_context.resource_config["port"]

    return create_engine(
        f"""mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}"""
    )