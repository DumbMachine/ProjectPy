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
interactive: True
default: True
git: True
colour: True
interactive: True

setup_py: True
setup_cfg: True
main: True
manifest: True
setup.cfg: True
docker: True
requirements: True
contributing: True
readme: 'markdown'

shields:
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
    # thing = yaml.load(custom, Loader=yaml.Loader)
    thing = yaml.load(open(location), Loader=yaml.Loader)

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

    conf = config.Config()
    print('gay', conf.options)
    for item in thing.keys():
        if item in files:
            conf.options['files'][item] = thing[item]
        # elif item in shields:
        elif item == 'shields':
            for small_item in thing[item].keys():
                conf.options['shields']['base'].append(small_item)
                conf.options['shields']['entity'].append(
                    thing[item][small_item])
        else:
            # try:
            conf.options[item] = thing[item]

    print(conf.options)
    return conf


def writer_writer(conf):
    '''
    Used to write shyat
    '''
    for writes in conf.options['files'].keys():
        if writes == 'license' and conf.options['files'][writes]:
            conf.actions[writes](
                f"./{conf.options['project_name']}", conf.options['files']['license'])

        try:
            conf.actions[writes](
                f"./{conf.options['project_name']}")
        except BaseException:
            # warnings.warn('Some error occured, clearing the folder')
            # shutil.rmtree(
            #     os.path.join('.', conf.options['project_name'])
            # )
            pass

        if writes == 'setup_py':
            conf.actions[writes](
                f"./{conf.options['project_name']}", conf.options)

        if writes == 'main':
            conf.actions[writes](
                f"./{conf.options['project_name']}", conf.options['project_name'])
    try:
        print(conf.options)
        from .generator import generate_README
        generate_README(os.path.join(
            '.', f"./{conf.options['project_name']}"), shields=conf.options['shields'])

    except Exception as e:
        print(e)
        raise RuntimeError('There was a problem generating the README.md')
