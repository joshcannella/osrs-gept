import click, json

from gept.catalog import Catalog

@click.command()
@click.argument("names", nargs=-1)
def hello(names):
    """Example script."""
    for name in names:
        click.echo(f"Hello {name}!")

@click.command(help="Look up items on the ge.")
@click.argument("args", nargs=-1) 
@click.option("-i", "--info", is_flag=True, show_default=True, default=False, help="Show item info.")
def find(args: str, info: bool):
    cat = Catalog()
    found = []
    for arg in args:
        found.extend(cat.search_by_name(arg))
    
    for item in found:
        click.echo(f"{item}{": " + json.dumps(item.json) if info else ""}")
    