# -*- coding: utf-8 -*-

'''The main package definition for Nuke 11.2v3.'''

# IMPORT THIRD-PARTY LIBRARIES
from rez.utils.lint_helper import alias
from rez.utils.lint_helper import env


name = 'nuke_installation'

version = '11.2v3'

description = 'Nuke 11.2v3'

authors = ['Foundry']

requires = ['respawn_includes-1.0.0']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT STANDARD LIBRARIES
    import os

    # IMPORT THIRD-PARTY LIBRARIES
    from rezzurect.utils import config_helper
    from rezzurect import chooser

    env.NUKE_INSTALL_ROOT = os.path.join('{root}', config_helper.INSTALL_FOLDER_NAME)

    if os.path.isdir(env.NUKE_INSTALL_ROOT.get()):
        env.PATH.append(env.NUKE_INSTALL_ROOT.get())

    chooser.add_common_commands(
        'nuke_installation',
        version=str(version),
        env=env,
        alias=alias,
    )


timestamp = 1537925779

format_version = 2
