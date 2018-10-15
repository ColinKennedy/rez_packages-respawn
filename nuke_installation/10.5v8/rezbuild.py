#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The main module which installs Nuke onto the user's system.'''

# IMPORT STANDARD LIBRARIES
import sys
import os

# IMPORT THIRD-PARTY LIBRARIES
from rez.utils import system
from rez import config


def build(source_path, build_path, install_path, targets):
    with system.add_sys_paths([config.config.package_definition_python_path]):
        # IMPORT THIRD-PARTY LIBRARIES
        from rezzurect import environment
        from rezzurect import chooser
        from rezzurect import manager

        # TODO : Get this information some better way
        package_install_path = os.path.join(install_path, 'install')
        version = os.environ['REZ_BUILD_PROJECT_VERSION']
        package_name = 'nuke_installation'

        environment.init(source_path, package_install_path)

        adapter = chooser.get_build_adapter(package_name, version)
        adapter.make_install()

        rezzurect_destination = os.path.join(install_path, 'python')
        manager.copy_rezzurect_to(rezzurect_destination)
