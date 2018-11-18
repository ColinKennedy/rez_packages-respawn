#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
import shutil
import sys
import os


def build(source_path, build_path, install_path, targets):
    '''Create a local copy of `rezzurect` into this Rez package.

    This copy will be used if the user's `REZZURECT_LOCATION` is not defined.

    Args:
        source_path (str):
            The absolute path to where this Rez package exists on-disk.
        build_path (str):
            The absolute path to the folder where this package's
            "build.rxt" file will be generated. Usually, this is a subdirectory
            inside of `source_path`.
        install_path (str):
            The absolute path of where `rezzurect` will be copied to.
        targets (list[str]):
            Optional arguments that are given by the user from the command-line.

    '''
    try:
        import rezzurect
    except ImportError:
        # Ideally, this should always be set but it's not required
        rezzurect_location = os.path.join(os.getenv('REZZURECT_LOCATION', ''), 'rezzurect')
    else:
        rezzurect_location = os.path.dirname(rezzurect.__file__)

    if not rezzurect_location or not os.path.isdir(rezzurect_location):
        return

    root_destination = os.path.join(install_path, 'python')

    if os.path.isdir(root_destination):
        shutil.rmtree(root_destination)
        os.makedirs(root_destination)

    destination = os.path.join(root_destination, os.path.basename(rezzurect_location))
    shutil.copytree(rezzurect_location, destination)


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:],
    )
