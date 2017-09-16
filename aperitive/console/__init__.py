# coding=utf-8
from __future__ import unicode_literals, absolute_import

import click

from aperitive.console.commander import Commander


@click.group()
@click.pass_context
def cli(ctx):
    pass


# Discover commands and add it to the `cli` group.
commander = Commander(cli)
commander.add_commands()


def main():
    cli(prog_name='aperitive')
