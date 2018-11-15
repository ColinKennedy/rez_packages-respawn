#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The main module which installs Maya onto the user's system.'''

# IMPORT STANDARD LIBRARIES
import sys
import os


def build(source_path, build_path, install_path, targets):
    pass


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:],
    )
