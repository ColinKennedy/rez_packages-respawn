# -*- coding: utf-8 -*-

name = 'respawn_includes'

version = '1.0.0'

description = ''

authors = ['ColinKennedy']

build_command = "python {root}/rezbuild.py {install}"


def commands():
    # IMPORT STANDARD LIBRARIES
    import inspect
    import sys
    import os

    # Ideally, this should always be set but it's not required
    rezzurect_location = os.getenv('REZZURECT_LOCATION', '')

    if not os.path.isdir(rezzurect_location):
        # From some reason, a Rez package.py doesn't let you do `os.path.realpath(__file__)
        # so we need to use the stack frame
        # And the stack frame returns as "</path/to/package.py:commands>"
        # so we need to strip parts of the returned string
        #
        package_path = inspect.getframeinfo(inspect.currentframe()).filename
        package_path = package_path[1:-1 * len(':commands>')]
        rezzurect_location = os.path.join(os.path.dirname(package_path), 'python')

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
