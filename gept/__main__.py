import click

from gept import commands

@click.group()
def cli():
    pass

cli.add_command(commands.find)
cli.add_command(commands.hello)