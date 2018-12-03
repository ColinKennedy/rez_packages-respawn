# -*- coding: utf-8 -*-

name = 'tank'

version = '1.0.0'

description = 'whatever'

authors = ['Shotgun Software']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    '''Create the environment variables and aliases needed to run this product.'''
    import platform
    import glob
    import os

    if platform.system() == 'Windows':
        _ROOT = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Shotgun')
    elif platform.system() == 'Linux':
        _ROOT = os.path.join(os.path.expanduser('~'), '.shotgun')
    else:
        raise NotImplementedError('Need the mac root folder, here')

    env.PYTHONPATH.append(
        sorted(glob.glob(os.path.join(
         _ROOT,
         'bundle_cache',
         'app_store',
         'tk-core',
         'v*',
         'python')))[-1]
    )