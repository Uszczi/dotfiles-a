import logging

import click

from .config import init_app
from .execute import execute_copy, execute_paste

log = logging.getLogger(__name__)


@click.command()
def copy():
    log.info("Copying files from disk to repo.")
    execute_copy()
    log.info("Done.")


@click.command()
def paste():
    log.info("Copying files from repo to disk.")
    execute_paste()
    log.info("Done.")


@click.group()
def cli():
    init_app("df")


cli.add_command(copy)
cli.add_command(paste)
