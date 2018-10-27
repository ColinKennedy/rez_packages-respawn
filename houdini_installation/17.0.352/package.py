# -*- coding: utf-8 -*-

'''The main package definition for Houdini 17.0.0352.'''

name = 'houdini_installation'

version = '17.0.0352'

description = 'Houdini 17.0.0352'

authors = ['SideFX']

install_root = 'install'

requires = ['respawn_includes-1.0.0']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT STANDARD LIBRARIES
    import os

    # IMPORT THIRD-PARTY LIBRARIES
    from rezzurect import chooser

    install_root = 'install'
    env.INSTALL_ROOT = os.path.join('{root}', install_root)

    chooser.add_common_commands(
        'houdini_installation',
        version=str(version),
        env=env,
        alias=alias,
    )


timestamp = 1537925779

format_version = 2
