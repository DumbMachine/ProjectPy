import os
import platform

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

def get_version():
    g = {}
    exec(open(os.path.join("{TEMPLATE}", "version.py")).read(), g)
    return g["__version__"]


setup(name="{TEMPLATE}",
      version="0.01",
      install_requires=required,
      packages=find_packages(exclude=["tests"]),
      scripts=[],
      description="CLI tool to create-python-packages",
      long_description="Longer Desciption of the sample plcakge folder",
      author="{AUTHOR}",
      author_email="P{AUTHOR_EMAIL}",
      maintainer="{AUTHOR}",
      maintainer_email="{AUTHOR_EMAIL}",
      url="https://github.com/{AUTHOR}/repo",
      download_url="https://github.com/{AUTHOR}/repo/releases",
      license="unlicensed",
      test_suite="tests",
      classifiers=[
          "Development Status :: 1 - Planning",
          # "Development Status :: 2 - Pre-Alpha",
          # "Development Status :: 3 - Alpha",
        #   "Development Status :: 4 - Beta",
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
          "Topic :: Software Development",
          "Topic :: Utilities",
      ],
	},
    platforms="Any"
)
