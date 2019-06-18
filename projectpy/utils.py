from __future__ import print_function

import readline
import os
import sys

from colorama import Back, Fore, Style, init

init(autoreset=True)


def cprint(something, somethingelse, somethingelsesomething, heading=False, normal=False):
    if normal:
        print()
        print(Fore.YELLOW+"%s%s%s" %
              (something, somethingelse, somethingelsesomething))
        print()
        return

    if heading:
        print()
        print(Fore.BLUE+"%s" % ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED+"%18s" % (somethingelse), end="")
        print(Fore.BLUE+"%18s" % ("||"), end="")

        # print(Fore.BLUE+"%1s"% ("||"), end="")
        print(Fore.RED+"%18s" % (somethingelsesomething), end="")
        print(Fore.BLUE+"%18s" % ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return

    else:
        print(Fore.BLUE+"%s" % ("||"), end="")

        print("%18s" % (somethingelse), end="")
        print(Fore.BLUE+"%18s" % ("||"), end="")

        print("%18s" % (somethingelsesomething), end="")
        print(Fore.BLUE+"%18s" % ("||"), end="\n")
        print("--------------------------------------------------------------------------")
        return


def copy_files(frem, to):
    import os
    return os.system("cp -rf %s %s" % (frem, to))


def files(no_custom=False):
    '''
    .gitignore files
    '''
    if not no_custom:
        return ['template', 'setup.py', 'setup.cfg', 'requirements.txt', 'README.md', 'LICENSE', '.gitignore',
                'optional/ci/.travis.yml', 'optional/MANIFEST.ini', 'optional/ci/appveyor.yml',
                'optional/.codecoveragerc', 'optional/dockerfile', 'optional/.codeclimate.yml']

    return ['template', 'setup.py', 'setup.cfg', 'requirements.txt', 'README.md', 'LICENSE', '.gitignore']


def progressBar(value, endvalue, message, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print(Fore.CYAN+"\rPercent: [{0}] {1}: {2} %".format(arrow + spaces,
                                                         int(round(percent * 100)), message), file=sys.stdout, end=" ")
    sys.stdout.flush()


def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result
