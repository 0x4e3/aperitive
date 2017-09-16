# coding=utf-8
from __future__ import unicode_literals

import os

from aperitive.console.utils import find_commands, load_command_class

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Commander(object):
    def __init__(self, cli):
        self.cli = cli

    def _load_commands(self):
        command_dir = os.path.join(BASE_DIR, 'console')
        command_names = find_commands(command_dir)
        commands = list(map(
            lambda cmd: load_command_class('aperitive', cmd),
            command_names))
        for command in commands:
            self.cli.add_command(command)

    def add_commands(self):
        self._load_commands()
