# coding=utf-8
from __future__ import unicode_literals

import six
import sys

from importlib import import_module


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated
    by the last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        msg = "%s doesn't look like a module path" % dotted_path
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])

    mod = import_module(module_path)

    try:
        return getattr(mod, class_name)
    except AttributeError:
        msg = 'Module "{}" does not define a "{}" attribute/class'.\
            format(module_path, class_name)
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])


def load_command_class(app_name, name):
    """
    Return command instance by given application name and command name.
    """
    return import_string(
        '{0}.console.commands.{1}.{1}'.format(app_name, name))
