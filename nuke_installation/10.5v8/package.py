# -*- coding: utf-8 -*-

'''The main package definition for Nuke 10.5v8.'''

name = 'nuke_installation'

version = '10.5v8'

description = 'Nuke 10.5v8'

authors = ['Foundry']

install_root = 'install'

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

    if os.path.isdir(env.INSTALL_ROOT.get()):
        env.PATH.append(env.INSTALL_ROOT.get())

    chooser.add_common_commands(
        'nuke_installation',
        version=str(version),
        env=env,
        alias=alias,
    )


timestamp = 1537925779

format_version = 2
