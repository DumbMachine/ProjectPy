This project was bootstrapped with [Create Python Project](https://github.com/DumbMachine/create-python-project).
⚫ The README is auto generated. It will help you get going with project.

# template
----

## For Basic Installation:
### Installation:
- The following will tell you 
  - Move to the main directory and run the following:
    ```bash
    $ python setup.py develop #If you are actively developing the package
    $ pip install . # or python setup.py install
    ```
### Uploading The Package to PYPI:
- Firstly make an account [here](https://pypi.org)
- Install Twine (This package will help you upload your package)
  ```bash
  $ pip install twine
  ```
  - Uploading a test package:
    - Creating a Distribution for you package:
	```bash
	$ python setup.py sdist bdist_wheel
	```
	- Uploading you Package to TestingPyPi (Enter your PYPI username and password when prompted):
    ```bash
	$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	username: .....
	password: *****
	```
  - Uploading the Final Package to PYPI:
  ```bash
  $ twine upload dist/*
  ```
- To check if the Package was uploaded Successfully:
```bash
$ pip install <package_name>
```
- If the package was uploaded, then a succesfull installation will occur.

## Custom Installation:
The below will help you setup, various testing and checking services for your code. You may skip this, if you wish. But it is recommendee.
### Getting the Badges:
- Visit the below links to add your repo to the various sites:
	- For CodeClimate:
		- [Visit here and add your repo](https://codeclimate.com/).
		- Grab your things badge from here.
	- For CodeCov [![Maintainability](https://api.codeclimate.com/v1/badges/3fa9da9a5e4e670d56bf/maintainability)](https://codeclimate.com/github/DumbMachine/create-python-project/maintainability)
		- [Visit here and add your repo](https://codecov.io/)
		- Grab your things badge from here.
	- For Travis [![Build Status](https://travis-ci.org/DumbMachine/create-python-project.svg?branch=master)](https://travis-ci.org/DumbMachine/create-python-project)
		- [Visit here and add your repo](https://travis-ci.org/)
		- Grab your things badge from here.
	- For AppVeyor [![Build status](https://ci.appveyor.com/api/projects/status/r73kob46x7rv690y?svg=true)](https://ci.appveyor.com/project/DumbMachine/create-python-project)
		- [Visit here and add your repo](https://ci.appveyor.com/signup)
		- Grab your things badge from here.
	- For Snyk Vulnerabilities [![Known Vulnerabilities](https://snyk.io/test/github/DumbMachine/create-python-project/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/DumbMachine/create-python-project?targetFile=requirements.txt)
		- [Visit here and add your repo](https://snyk.io/)
		- Grab your things badge from here.
### Installation:
- Move to the main directory and run the following:
```bash
$ python setup.py develop #If you are actively developing the package
$ pip install . # or python setup.py install
```
### Uploading The Package to PYPI:
- Firstly make an account [here](https://pypi.org)
- Install Twine (This package will help you upload your package)
  ```bash
  $ pip install twine
  ```
  - Uploading a test package:
    - Creating a Distribution for you package:
	```bash
	$ python setup.py sdist bdist_wheel
	```
	- Uploading you Package to TestingPyPi (Enter your PYPI username and password when prompted):
    ```bash
	$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	username: .....
	password: *****
	```
  - Uploading the Final Package to PYPI:
  ```bash
  $ twine upload dist/*
  ```
- To check if the Package was uploaded Successfully:
```bash
$ pip install <package_name>
```
- If the package was uploaded, then a succesfull installation will occur.
- 