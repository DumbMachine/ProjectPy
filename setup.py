import os
import platform

from setuptools import find_packages, setup

# ? To Copy the Template Data
temp = [f for f in os.walk('./projectpy/template')]
files = []
for tempy in temp:
    base = tempy[0]
    for somethingelse in tempy[1:]:
        for something in somethingelse[:]:
            files.append(os.path.join(tempy[0], something))
files = [file.replace('./projectpy/', './') for file in files]


with open('./requirements.txt') as f:
    required = f.read().splitlines()


def get_version():
    g = {}
    exec(open(os.path.join("projectpy", "version.py")).read(), g)
    return g["__version__"]


setup(name="projectpy",
      version=get_version(),
      install_requires=required,
      packages=find_packages(exclude=["tests"]),
      scripts=[],
      description="CLI tool to create-python-packages",
      long_description="Longer Desciption of the sample plcakge folder",
      author="Ratin Kumar",
      author_email="ratin.kumar.2k@gmail.com",
      maintainer="Ratin Kumar (@DumbMachine)",
      maintainer_email="ratin.kumar.2k@gmail.com",
      url="https://github.com/DumbMachine/create-python-project",
      download_url="https://github.com/DumbMachine/create-python-project/releases",
      license="unlicensed",
      test_suite="tests",
      # install_requires = ["numpy>=1.13.1"],
      # setup_requires = ["pytest-runner"],
      # tests_require = ["pytest"],
      classifiers=[
          #   "Development Status :: 1 - Planning",
          # "Development Status :: 2 - Pre-Alpha",
          "Development Status :: 3 - Alpha",
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
      entry_points={
          'console_scripts': [
              'projectpy = projectpy.cli:run_as_command',
          ],
      },
      platforms="Any",
      package_data={'projectpy': files},
      )
