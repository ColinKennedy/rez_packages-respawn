#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The main module which installs Nuke onto the user's system.'''

# IMPORT STANDARD LIBRARIES
import sys
import os


def build(source_path, build_path, install_path, targets):
    # IMPORT THIRD-PARTY LIBRARIES
    from rezzurect.utils import config_helper
    from rezzurect import environment
    from rezzurect import chooser
    from rezzurect import manager

    # TODO : Get this information some better way
    package_install_path = os.path.join(install_path, config_helper.INSTALL_FOLDER_NAME)
    version = os.environ['REZ_BUILD_PROJECT_VERSION']

    environment.init(source_path, package_install_path)

    adapter = chooser.get_build_adapter('nuke_installation', version)
    adapter.make_install()

    rezzurect_destination = os.path.join(install_path, 'python')
    manager.copy_rezzurect_to(rezzurect_destination)


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:],
    )
