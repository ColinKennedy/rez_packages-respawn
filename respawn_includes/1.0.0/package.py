#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The main package which makes `rezzurect` shareable with other packages.'''

# IMPORT THIRD-PARTY LIBRARIES
from rez.utils.lint_helper import alias
from rez.utils.lint_helper import env

name = 'respawn_includes'

version = '1.0.0'

description = ''

authors = ['ColinKennedy']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    # IMPORT STANDARD LIBRARIES
    import sys
    import os

    paths = os.getenv('RESPAWN_PYTHONPATH', '')

    if paths:
        additional_python_paths = paths.split(os.pathsep)

        # Any Rez package that adds this package into `requires` will need to
        # have these paths added to `sys.path`. Otherwise, package.py will fail
        #
        sys.path.extend(additional_python_paths)

        try:
            import rezzurect  # Make sure that the user added `rezzurect` to RESPAWN_PYTHONPATH
        except ImportError:
            # If they did not, default to the copied `rezzurect`
            current_dir = os.path.dirname(os.path.realpath('__file__'))
            sys.path.append(os.path.join(current_dir, 'python'))

        # And we need to add the same paths to `env.PYTHONPATH` or `rezbuild.py`
        # commands will fail to import `rezzurect`
        #
        for path in additional_python_paths:
            env.PYTHONPATH.append(path)
    else:
        current_dir = os.path.dirname(os.path.realpath('__file__'))
        sys.path.append(os.path.join(current_dir, 'python'))
