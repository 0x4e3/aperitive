#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='aperitive',
    version='0.1.0',
    description="Python CLI utility for creation new projects for "
                "GitLab/Redmine/Slack/Sentry stack.",
    long_description=readme + '\n\n' + history,
    author="Alexander Lebedev",
    author_email='lebedev@0x4e3.ru',
    url='https://github.com/0x4e3/aperitive',
    packages=find_packages(include=['aperitive']),
    entry_points={
        'console_scripts': [
            'aperitive=aperitive.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='aperitive',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
