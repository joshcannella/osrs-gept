import click

from gept import commands

@click.group()
def cli():
    """

    OSRS GE Price Tracker.
    A tiny cli that looks up OSRS Grand Exchange prices.

    """

cli.add_command(commands.search)
cli.add_command(commands.hello)