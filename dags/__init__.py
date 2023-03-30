from dagster import load_assets_from_modules, repository
import example_dag


@repository(name="EXAMPLE")
def example():

    example_assets = load_assets_from_modules(
        modules=[example],
        group_name="EXAMPLE"
    )

    return [
        [*example_assets]
    ]
