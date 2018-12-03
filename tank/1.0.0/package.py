# -*- coding: utf-8 -*-

name = 'tank'

version = '1.0.0'

description = 'whatever'

authors = ['Shotgun Software']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    env.PYTHONPATH.append('/home/selecaoone/.shotgun/shenanigans/p87c36.basic.desktop/cfg/install/core/python')
