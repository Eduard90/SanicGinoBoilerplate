import click
from system.click import AutoImportGroup


@click.group(cls=AutoImportGroup, help="Subcommands to work with database", filepath=__file__)
def db():
    pass
