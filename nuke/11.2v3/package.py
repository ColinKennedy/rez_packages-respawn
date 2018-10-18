# -*- coding: utf-8 -*-

'''The main package definition for Nuke 11.2v3.'''

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
    pass


timestamp = 1537925779

format_version = 2
