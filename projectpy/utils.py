from __future__ import print_function

import readline
import os
import sys
import yaml
from colorama import Back, Fore, Style, init

init(autoreset=True)

files = [
    "license",
    "git",
    "color",
    "requirements",
    "tests",
    "main",
    "contributing",
    "interactive",
    "manifest",
    "setup_cfg",
    "setup_py",
    "dockerfile",
    "readme",
]

shields = [
    "build",
    "codecov",
    "analysis",
    "chat",
    "dependencies",
    "size",
    "downloads",
    "funding",
    "issues",
    "license",
    "rating",
    "social",
    "version",
    "platform",
    "monitoring",
    "activity",
    "other",
    "custom_shield",
]


def cprint(
        something,
        somethingelse,
        somethingelsesomething,
        heading=False,
        normal=False):
    if normal:
        print()
        print(Fore.YELLOW + "%s%s%s" %
              (something, somethingelse, somethingelsesomething))
        print()
        return

    if heading:
        print()
        print(Fore.BLUE + "%s" % ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED + "%18s" % (somethingelse), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED + "%18s" % (somethingelsesomething), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return

    else:
        print(Fore.BLUE + "%s" % ("||"), end="")

        print("%18s" % (somethingelse), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="")

        print("%18s" % (somethingelsesomething), end="")
        print(Fore.BLUE + "%18s" % ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return


def copy_files(frem, to):
    import os
    return os.system("cp -rf %s %s" % (frem, to))


# def files(no_custom=False):
#     '''
#     .gitignore files
#     '''
#     if not no_custom:
#         return [
#             'template',
#             'setup.py',
#             'setup.cfg',
#             'requirements.txt',
#             'README.md',
#             'LICENSE',
#             '.gitignore',
#             'optional/ci/.travis.yml',
#             'optional/MANIFEST.ini',
#             'optional/ci/appveyor.yml',
#             'optional/.codecoveragerc',
#             'optional/dockerfile',
#             'optional/.codeclimate.yml']

#     return [
#         'template',
#         'setup.py',
#         'setup.cfg',
#         'requirements.txt',
#         'README.md',
#         'LICENSE',
#         '.gitignore']


def progressBar(value, endvalue, message, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print(Fore.CYAN +
          "\rPercent: [{0}] {1}: {2} %".format(arrow +
                                               spaces, int(round(percent *
                                                                 100)), message), file=sys.stdout, end=" ")
    sys.stdout.flush()


def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


def custom_reader(location):
    custom = '''project_name: 'PrjectGetGPA'
project_version: 0.01alpha
project_description: 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'
author_name: 'Ratin Kumar'
github_username: 'DumbMachine'

default: False

license: 'MIT'
git: True
colour: True
interactive: False
default: False
license: 'MIT'
git: True
colour: True
interactive: False

setup_py: True
setup_cfg: True
main: True
manifest: False
setup.cfg: False
docker: False
requirements: True
contributing: True
readme: 'markdown'

build: 'appveyor'
codecov: 'codecov'
analysis: 'gtihub-lanugage-count'
chat: 'discord'
dependencies:
size: 'github-repo-size'
downloads:
funding:
issues:
license: 'github'
rating:
social:
version: 'pypi'
platform:
monitoring:
activity:
other:
'''
    thing = yaml.load(custom, Loader=yaml.Loader)

    files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "interactive",
        "manifest",
        "setup_cfg",
        "setup_py",
        "dockerfile",
        "readme",
    ]

    shields = [
        "build",
        "codecov",
        "analysis",
        "chat",
        "dependencies",
        "size",
        "downloads",
        "funding",
        "issues",
        "license",
        "rating",
        "social",
        "version",
        "platform",
        "monitoring",
        "activity",
        "other",
        "custom_shield",
    ]

    conf = Config()
    for item in thing.keys():
        if item in files:
            conf.all['files'][item] = thing[item]
        elif item in shields:
            conf.all['shields']['base'].append(item)
            conf.all['shields']['entity'].append(thing[item])
        else:
            # try:
            conf.all[item] = thing[item]

    print(conf.all)
    return conf.all


# {
#     'default': False,
#     'config_location': '.',
#     'display_options': True,
#     'clear_directory': False,
#     'project_name': 'PrjectGetGPA',
#     'project_version': '0.01alpha',
#     'project_description': 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.',
#     'author_name': 'Ratin Kumar',
#     'author_email': 'placeholder.com',
#     'github_username': 'DumbMachine',
#     'license': 'MIT',
#     'files': {
#         'license': 'github',
#         'git': True,
#         'color': True,
#         'requirements': True,
#         'tests': True,
#         'main': True,
#         'contributing': True,
#         'interactive': False,
#         'manifest': False,
#         'setup_cfg': True,
#         'setup_py': True,
#         'dockerfile': False,
#         'readme': 'markdown'},
#     'shields': {
#         'base': [
#             'build',
#             'codecov',
#             'analysis',
#             'chat',
#             'dependencies',
#             'size',
#             'downloads',
#             'funding',
#             'issues',
#             'rating',
#             'social',
#             'version',
#             'platform',
#             'monitoring',
#             'activity',
#             'other'],
#         'entity': [
#             'appveyor',
#             'codecov',
#             'gtihub-lanugage-count',
#             'discord',
#             None,
#             'github-repo-size',
#             None,
#             None,
#             None,
#             None,
#             None,
#             'pypi',
#             None,
#             None,
#             None,
#             None]},
#     'colour': True,
#     'setup.cfg': False,
#     'docker': False}
