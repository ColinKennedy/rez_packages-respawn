# -*- coding: utf-8 -*-

'''The main package definition for Houdini 16.5.536.'''

name = 'houdini_installation'

version = '16.5.536'

description = 'Houdini 16.5.536'

authors = ['Foundry']

install_root = 'install'

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT STANDARD LIBRARIES
    import os

    # IMPORT THIRD-PARTY LIBRARIES
    from rez.utils import system
    from rez import config

    with system.add_sys_paths([config.config.package_definition_python_path]):
        from rezzurect import chooser

        install_root = 'install'
        install_folder = os.path.join('{root}', install_root)
        env.INSTALL_ROOT = install_folder

        if os.path.isdir(env.INSTALL_ROOT.get()):
            env.PATH.append(env.INSTALL_ROOT.get())

        chooser.add_common_commands(
            'houdini_installation',
            version=str(version),
            env=env,
            alias=alias,
        )


timestamp = 1537925779

format_version = 2
