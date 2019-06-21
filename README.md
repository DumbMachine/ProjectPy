# ProjectPy



![](https://user-images.githubusercontent.com/23381512/58745622-a0c55000-8470-11e9-803d-98048a386ce9.png)

## Getting Started:

A Simple **create-react-app** like CLI tool to create Python Package File Structure.

It offers the current features:

* Super Easy to use cli.
* One Command installation for Simple Python Packages.
* Customizable config for awesome Python Packages.
* Minimal worries about project structure.
* No dependencies.

## Installation

### Install from PyPI:

```bash
$ pip install projectpy
```

### Install from Source:

* Clone this repository and install the package:

```bash
$ git clone https://github.com/DumbMachine/ProjectPy
$ cd projectpy
$ python setup.py install
```

## Basic Usage

Creating a simple Python Package with default settings is as simple as:

```bash
$ projectpy -n ExamplePackage
---------------------------------------------------------------------------------------
PROJECTPY: A Python CLI to create packages
Creating ExamplePackage with the following config:

project_name: ExamplePackage
project_version: 0.01
project_description: "This is the default Placeholder description"
author_name: "Placeholder:author_name"
github_username: "Placeholder:github_username"
github_email: "Placeholder:github_email"

license: "MIT"
git: True
color: True
requirements: True
readme: "markdown"
contributing.md: True
interactive: False

shields:
  build: "appveyor"
  chat: "discord"
  license: "github"
  extras: "pypi---downloads"
  
🌟 Done in 3 seconds.
✅ Success created Example_Repo in ~/Example_Repo

    ______________________________
    |                            |
    | Generation was successful  |
    | -------------------------  |
    | $ cd ExamplePackage        |
    | $ python setup.py install  |
    ------------------------------
    
👋 bai bai    
```

This will create a directory **ExampleDirectory** with the following Tree structure:

```bash
$ tree ExamplePackage/
----------------------------------------------------------------------------------------
ExamplePackage
├── contributing.md
├── ExamplePackage
    └── __init__.py
├── LICENSE
├── MANIFEST.ini
├── README.md
├── requirements.txt
├── setup.py
└── tests
    └── __init__.py
```

{% hint style="success" %}
The Package is now ready to be installed.
{% endhint %}

**To Install the package:**

```bash
$ cd ExamplePackage
$ python setup.py install

# To check the installation, try importing the installed package.
$ python
Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ExamplePackage
🎉 Successfull Installation
```

The message at the end "🎉 Successfull Installation " shows that the package was installed successfully.

