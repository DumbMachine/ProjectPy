# 🔴 THIS DOCUMENTATION IS WIP and will be completed soon.

![image](https://user-images.githubusercontent.com/23381512/58745622-a0c55000-8470-11e9-803d-98048a386ce9.png)

# create-python-project
[![Build status](https://ci.appveyor.com/api/projects/status/r73kob46x7rv690y?svg=true)](https://ci.appveyor.com/project/DumbMachine/create-python-project) [![Build Status](https://travis-ci.org/DumbMachine/create-python-project.svg?branch=master)](https://travis-ci.org/DumbMachine/create-python-project) [![Maintainability](https://api.codeclimate.com/v1/badges/3fa9da9a5e4e670d56bf/maintainability)](https://codeclimate.com/github/DumbMachine/create-python-project/maintainability) [![Known Vulnerabilities](https://snyk.io/test/github/DumbMachine/create-python-project/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/DumbMachine/create-python-project?targetFile=requirements.txt)

A Simple **create-react-app**
like CLI tool to create Python Project File Structure.

## Get Started Immediately:
- Minimal worries about project structure.
- Gives many options for customization.

# Installation:
## Install from PYPI:
```bash
$ pip install projectpy
```
## Install from Source:
- Clone this repository and install the package:
```bash
$ git clone https://github.com/DumbMachine/create-python-project
$ cd create-python-project
$ python setup.py install
```

# Usage:
## Minimal Installation:
- This method is best for those who want to create a bare-bone simple Python Package, which is ready to *pip install* and *uploading to PYPI* .
- Using the CLI:
```bash
$ projectpy -n Example_Repo --config

PROJECTPY: A Python CLI to create packages
Percent: [----------------------->] 100: Copying file optional/.codec % 

||            Option                ||            Choice                ||
--------------------------------------------------------------------------
||         repo_name                ||      Example_Repo                ||
--------------------------------------------------------------------------
||         license                  ||      unilicense                  ||
--------------------------------------------------------------------------
||    cintergrations                ||          None                    ||
--------------------------------------------------------------------------
||            config                ||          True                    ||
--------------------------------------------------------------------------
||             color                ||          True                    ||
--------------------------------------------------------------------------
||             clean                ||          False                   ||
--------------------------------------------------------------------------
||               git                ||          False                   ||
--------------------------------------------------------------------------

🌟 Done in 5 seconds.
Success created Example_Repo in ~/Example_Repo

Begin by doing the follwing:
$ cd  Example_Repo

To develop and work on the Package:
$ python setup.py develop

TO install the Package:
$ python setup.py install

👋 bai bai
```
- Installing the Example_Repo
```bash
$ cd Example_Repo
$ python setup.py install
```
- The above will create the following Tree Structure in Example_Repo:
```bash
$ tree Example_Repo
Example_Repo
├── LICENSE
├── Example_Repo
│   ├── __init__.py
│   └── temp.py
├── README.md
├── requirements.txt
├── setup.cfg
└── setup.py

1 directory, **7** files
```
- To test the install, open the Python in any directory:
```python
In [1]: import Example_Repo 
Out[1]: The Installation was Sucessful.
        For future information visit https://github.com/DumbMachine/create-python-project
```
- If you see the above then, your Installation was Successfull.

## Custom Installation:
- This is the recommended was of using this CLI.
- This method will supply your package repo with files for Services like Testing, Continuous Integration with Travis/Tox/Jenkins.
```
$ projectpy -n Example_Repo --config -ci travis -git --license unilicense

PROJECTPY: A Python CLI to create packages
Percent: [----------------------->] 100: Copying file optional/.codec % 

||            Option                ||            Choice                ||
--------------------------------------------------------------------------
||         repo_name                ||      Example_Repo                ||
--------------------------------------------------------------------------
||         license                  ||      unilicense                  ||
--------------------------------------------------------------------------
||    cintergrations                ||          Travis                  ||
--------------------------------------------------------------------------
||            config                ||          True                    ||
--------------------------------------------------------------------------
||             color                ||          True                    ||
--------------------------------------------------------------------------
||             clean                ||          False                   ||
--------------------------------------------------------------------------
||               git                ||          True                    ||
--------------------------------------------------------------------------

🌟 Done in 5 seconds.
Success created Example_Repo in ~/Example_Repo

Begin by doing the follwing:
$ cd  Example_Repo

To develop and work on the Package:
$ python setup.py develop

TO install the Package:
$ python setup.py install

👋 bai bai
```
- Installing the Example_Repo
```bash
$ cd Example_Repo
$ python setup.py install
```
- Tree:
```bash
$ tree Example_Repo
Example_Repo
├── appveyor.yml
├── .codeclimate.yml
├── .codecoveragerc
├── dockerfile
├── .gitignore
├── LICENSE
├── MANIFEST.ini
├── Example_Repo
│   ├── __init__.py
│   └── temp.py
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
└── .travis.yml

1 directory, 14 files
```
# 🗒 TODO:
- [ ] Add support for Logging.
- [ ] Improve the CLI ( Add more colors )
- [ ] Make examples for showing the thing.
- [ ] Add support for Jenkins