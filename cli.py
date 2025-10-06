#!/usr/bin/env python
import click
from polarbadge.parties.pp33 import cli as pp33_cli


@click.group()
def cli():
    pass


cli.command(pp33_cli.pp33_everyone)
cli.command(pp33_cli.pp33_users)
cli.command(pp33_cli.register)


if __name__ == "__main__":
    cli()