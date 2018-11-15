# -*- coding: utf-8 -*-

'''The main package definition for Nuke 11.2v3.'''

# IMPORT THIRD-PARTY LIBRARIES
from rez.utils.lint_helper import alias
from rez.utils.lint_helper import env


name = 'nuke'

version = '11.2v3'

description = 'Nuke 11.2v3'

authors = ['Foundry']

requires = [
    'nuke_installation-{version}'.format(version=version),
]

install_root = 'install'

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT THIRD-PARTY LIBRARIES
    from rez.utils import system
    from rez import config

    with system.add_sys_paths([config.config.package_definition_python_path]):
        from rezzurect import chooser

        chooser.add_common_commands(
            'nuke',
            version=str(version),
            env=env,
            alias=alias,
        )


timestamp = 1537925779

format_version = 2
