import click

from .execute import execute_copy, execute_paste


@click.command()
def copy():
    click.echo("Start coping files to repo.")
    execute_copy()
    click.echo("Done.")


@click.command()
def paste():
    click.echo("Start coping files from repo to computer.")
    execute_paste()
    click.echo("Done.")


@click.group()
def cli():
    pass


cli.add_command(copy)
cli.add_command(paste)
