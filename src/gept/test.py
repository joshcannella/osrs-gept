import click
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# List of cities for autocompletion
cities = ['New York', 'London', 'Paris', 'Tokyo']
city_completer = WordCompleter(cities)

# Custom prompt function with autocompletion
def prompt_with_autocompletion(prompt_text, completer=None):
    return prompt(prompt_text, completer=completer)

@click.command()
@click.option('--name', prompt='Your name', help='Your name')
def greet(name):
    city = prompt_with_autocompletion('Your city: ', completer=city_completer)
    click.echo(f"Hello, {name} from {city}!")

if __name__ == '__main__':
    greet()
