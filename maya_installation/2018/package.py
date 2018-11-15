# -*- coding: utf-8 -*-

'''The main package definition for Nuke 10.5v8.'''

# IMPORT THIRD-PARTY LIBRARIES
from rez.utils.lint_helper import alias
from rez.utils.lint_helper import env


name = 'maya_installation'

version = '2018'

description = 'Maya 2018'

authors = ['Autodesk']

requires = ['respawn_includes-1.0.0']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT STANDARD LIBRARIES
    import os

    # IMPORT THIRD-PARTY LIBRARIES
    from rezzurect.utils import config_helper
    from rezzurect import chooser

    env.INSTALL_ROOT = os.path.join('{root}', config_helper.INSTALL_FOLDER_NAME)

    if os.path.isdir(env.INSTALL_ROOT.get()):
        env.PATH.append(env.INSTALL_ROOT.get())

    chooser.add_common_commands(
        'maya_installation',
        version=str(version),
        env=env,
        alias=alias,
    )


timestamp = 1537925779

format_version = 2
