# -*- coding: utf-8 -*-

'''The main package definition for Houdini 16.5.536.'''

name = 'houdini'

version = '16.5.536'

description = 'Houdini 16.5.536 - Production Build'

authors = ['SideFX']

requires = [
    'houdini_installation-{version}'.format(version=version),
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    # IMPORT THIRD-PARTY LIBRARIES
    from rezzurect import chooser

    chooser.add_common_commands(
        'houdini',
        version=str(version),
        env=env,
        alias=alias,
    )


timestamp = 1537925779

format_version = 2
