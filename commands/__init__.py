import click
from system.click import CommandGroup


@click.group(cls=CommandGroup, filepath=__file__)
def cli():
    pass
