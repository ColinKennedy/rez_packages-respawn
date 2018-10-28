# -*- coding: utf-8 -*-

'''The main package definition for Houdini 16.5.536.'''

# IMPORT THIRD-PARTY LIBRARIES
from rez.utils.lint_helper import alias
from rez.utils.lint_helper import env


name = 'houdini_installation'

version = '16.5.536'

description = 'Houdini 16.5.536'

authors = ['SideFX']

requires = ['respawn_includes-1.0.0']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT STANDARD LIBRARIES
    import os

    # IMPORT THIRD-PARTY LIBRARIES
    from rezzurect.utils import rezzurect_config
    from rezzurect import chooser

    env.INSTALL_ROOT = os.path.join('{root}', rezzurect_config.INSTALL_FOLDER_NAME)

    chooser.add_common_commands(
        'houdini_installation',
        version=str(version),
        env=env,
        alias=alias,
    )


timestamp = 1537925779

format_version = 2
