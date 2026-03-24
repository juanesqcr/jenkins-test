import click

@click.command()
@click.option("--name", default="World", help="Nombre a saludar")
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello()