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

    additional_python_paths = os.getenv('RESPAWN_PYTHONPATH', '').split(os.pathsep)
    sys.path.extend(additional_python_paths)  # TODO : Check if I need this line. Delete if not

    for path in additional_python_paths:
        env.PYTHONPATH.append(path)
