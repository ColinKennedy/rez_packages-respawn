#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
import sys
import os


def build(source_path, build_path, install_path, targets):
    # IMPORT STANDARD LIBRARIES
    import sys
    import os

    paths = os.getenv('RESPAWN_PYTHONPATH', '')

    if not paths:
        return

    additional_python_paths = paths.split(os.pathsep)

    # Any Rez package that adds this package into `requires` will need to
    # have these paths added to `sys.path`. Otherwise, package.py will fail
    #
    sys.path.extend(additional_python_paths)

    from rezzurect import manager

    rezzurect_destination = os.path.join(install_path, 'python')
    manager.copy_rezzurect_to(rezzurect_destination)


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:],
    )
