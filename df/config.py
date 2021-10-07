import logging

import click


def init_logger(name):
    class DotHandler(logging.Handler):
        def emit(self, record):
            msg = self.format(record)
            click.echo(msg)

    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    handler = DotHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)

    log.addHandler(handler)


def init_app(name):
    init_logger(name)
