# coding=utf-8
from __future__ import unicode_literals

import os
import pkgutil

import six
import sys

if six.PY2:
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()


def npath(path):
    """
    Always return a native path, that is unicode on Python 3 and byte string
    on Python 2.
    """
    if six.PY2 and not isinstance(path, bytes):
        return path.encode(fs_encoding)
    return path


def find_commands(management_dir):
    """
    Given a path to a management directory, returns a list of all the command
    names that are available.

    Returns an empty list if no commands are defined.
    """
    command_dir = os.path.join(management_dir, 'commands')
    return [name for _, name, is_pkg in
            pkgutil.iter_modules([npath(command_dir)])
            if not is_pkg and not name.startswith('_')]
