from dagster import load_assets_from_modules, repository
import hello_world, hi_user

# A sample repository
@repository(name="SAMPLE")
def example():

    example_assets = load_assets_from_modules(
        modules=[hello_world, hi_user],
        group_name="examples"
    )

    return [
        [*example_assets]
    ]
