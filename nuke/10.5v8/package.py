# -*- coding: utf-8 -*-

'''The main package definition for Nuke 10.5v8.'''

name = 'nuke'

version = '10.5v8'

description = 'Nuke 10.5v8'

authors = ['Foundry']

requires = [
    'nuke_installation-{version}'.format(version=version),
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    pass


timestamp = 1537925779

format_version = 2
