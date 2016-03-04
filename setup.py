#!/usr/bin/env python3
# Note that this script only installs the python modules,
# the other parts of crmsh are installed by autotools
from distutils.core import setup
import os

SRC_PATH = os.path.relpath(os.path.join(os.path.dirname(__file__), "crmsh"))

setup(name='crmsh',
      version='2.2.0',
      description='Command-line interface for High-Availability cluster management',
      author='Kristoffer Gronlund',
      author_email='kgronlund@suse.com',
      url='http://crmsh.github.io/',
      packages=['crmsh'],
      package_dir={'crmsh': SRC_PATH})
