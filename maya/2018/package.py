# -*- coding: utf-8 -*-

'''The main package definition for Maya 10.5v8.'''

name = 'maya'

version = '2018'

description = 'Maya 2018'

authors = ['Autodesk']

requires = [
    'maya_installation-{version}'.format(version=version),
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    pass


timestamp = 1537925779

format_version = 2
