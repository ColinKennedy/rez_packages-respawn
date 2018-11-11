#!/usr/bin/env python
#

name = 'respawn_includes'

version = '1.0.0'

description = ''

authors = ['ColinKennedy']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    # IMPORT STANDARD LIBRARIES
    import sys
    import os

    rezzurect_location = os.environ['REZZURECT_LOCATION']
    sys.path.append(rezzurect_location)
    env.PYTHONPATH.append(rezzurect_location)

    additional_python_paths = os.getenv('RESPAWN_PYTHONPATH', '').split(os.pathsep)

    # Any Rez package that adds this package into `requires` will need to
    # have these paths added to `sys.path`. Otherwise, package.py will fail
    #
    sys.path.extend(additional_python_paths)

    # And we need to add the same paths to `env.PYTHONPATH` or `rezbuild.py`
    # commands will fail to import `rezzurect`
    #
    for path in additional_python_paths:
        env.PYTHONPATH.append(path)
