import click        

from gept.catalog import Catalog

@click.command()
@click.option("-i", "--info", is_flag=True, show_default=True, default=False, help="Show item info.")
@click.argument("items", nargs=-1)
def hello(info, items):
    """Example script."""
    for item in items:
        click.echo(f"Hello {item}{" (info)" if info else ""}!")

@click.command(help="Look up items on the ge.")
@click.argument("input")   
def find(input):
    cat = Catalog()
    click.echo(cat.search_by_name(input))