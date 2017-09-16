# coding=utf-8
from __future__ import unicode_literals

import os

from pkg_resources import resource_string

import click


CONFIG_FILE = '.aperitive.yml'


@click.command()
@click.argument('directory', required=False, nargs=1)
@click.option('--gitlab-server', prompt=True)
@click.option('--gitlab-user', prompt=True)
@click.option('--gitlab-user-password', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.option('--redmine-server', prompt=True)
@click.option('--redmine-user', prompt=True)
@click.option('--redmine-user-password', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.option('--echo', is_flag=True,
              help='Write config to the stdout, not to the file.')
@click.pass_context
def init(ctx, directory, gitlab_server, gitlab_user, gitlab_user_password,
         redmine_server, redmine_user, redmine_user_password, echo):
    """
    Initializes aperitive configuration.
    """
    if directory:
        if not os.path.exists(directory):
            click.confirm('Configuration directory {} does not exist, '
                          'create it for you?'.format(directory), abort=True)
            try:
                os.makedirs(directory)
            except IOError as e:
                click.ClickException(
                    'Unable to create directory {}: {}'.format(
                        directory, repr(e)))
        if not os.path.isdir(directory):
            return click.ClickException(
                '{0} is not a directory.'.format(directory))
    else:
        directory = '~/'

    config_context = {
        'gitlab_server': gitlab_server,
        'gitlab_user': gitlab_user,
        'gitlab_user_password': gitlab_user_password,
        'redmine_server': redmine_server,
        'redmine_user': redmine_user,
        'redmine_user_password': redmine_user_password,
    }
    config_content = resource_string(
        'aperitive',
        'data/aperitive.yml.template').decode('utf-8') % config_context

    if echo:
        click.echo(config_content)
        click.confirm('Do you want to write this configuration to the file?',
                      abort=True)

    directory = os.path.expanduser(directory)
    config = os.path.join(directory, CONFIG_FILE)

    if os.path.isfile(config):
        click.confirm(
            'Configuration file already exists at {}, '
            'overwrite?'.format(click.format_filename(config)), abort=True)

    with click.open_file(config, 'w') as config_file:
        config_file.write(config_content)
