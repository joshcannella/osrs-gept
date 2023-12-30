import click

@click.command()
@click.option("-i", "--info", is_flag=True, show_default=True, default=False, help="Show item info.")
@click.argument("items", nargs=-1)
def main(info, items):
    """Example script."""
    for item in items:
        click.echo(f"Hello {item}{" (info)" if info else ""}!")