#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `aperitive` package."""
import os

import yaml

from click.testing import CliRunner

from aperitive import console


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(console.cli)
    assert result.exit_code == 0
    assert 'Usage: ' in result.output
    help_result = runner.invoke(console.cli, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_init():
    runner = CliRunner()

    command_input = 'gitlab.com\napiuser\npwd\npwd' \
                    '\nredmine.com\napiuser\npwd\npwd'

    # Test 'init' command in the isolated filesystem and
    # custom config directory.
    with runner.isolated_filesystem():
        config_dir = './config'
        config_file = os.path.join(config_dir, '.aperitive.yml')

        result = runner.invoke(
            console.cli,
            ['init', config_dir],
            input=command_input + '\ny')
        assert not result.exception

        assert os.path.exists(config_dir) and os.path.isdir(config_dir)

        assert os.path.exists(config_file) and os.path.isfile(config_file)

        with open(config_file) as f:
            config = yaml.load(f)
            assert config['gitlab.server'] == 'gitlab.com'
            assert config['redmine.server'] == 'redmine.com'
