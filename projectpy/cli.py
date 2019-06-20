import argparse
import json
import os
import shutil
import site
import sys
import textwrap
import time
import warnings

from colorama import Fore, init

from . import config, utils
from .config import Config
from .generator import generate_README
from .writer import *

init(autoreset=True)


def options():
    '''
    Parsing the Arguments here
    '''
    ap = argparse.ArgumentParser(
        prog="projectpy",
        usage="%(prog)s [options]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''PROJECTPY
                                       =========================
                                       - A create-python-package CLI
                                       =========================
                                       '''))

    ap.add_argument("-n", "--name", required=False, help="Name of the project")

    ap.add_argument(
        "-d",
        "--default",
        required=False,
        help="Minimilastic Installation",
        default=True)

    ap.add_argument(
        "-c",
        "--config",
        required=False,
        help="Location of the config.yaml/config.yml file",
        default=False)

    ap.add_argument(
        "-dis",
        "--display",
        required=False,
        help="Displays the Current Config",
        default=True)

    ap.add_argument(
        "-col",
        "--color",
        required=False,
        help="Toggle Colors on the print",
        default=True)

    ap.add_argument(
        "-clr",
        "--clean",
        required=False,
        help="Delete folder with same name if it exits",
        default=False)

    ap.add_argument(
        "-i",
        "--interactive",
        required=False,
        help="Get an Interactive prompt to fill the forms.",
        default=False)

    return vars(ap.parse_args())


def initialize(args):
    '''
    Sets the Config for the installation

    @params:
        args: argparse.ArguementParser
            : The arguments parsed by the CLI
    '''
    conf = config.Config()

    if args['config']:
        print('CUSTOM\n')

        return utils.custom_reader(args['config'])

    elif args['default']:
        print('DEFAULT\n')
        conf.options['project_name'] = args['name']
        conf.options['default'] = args['default']
        conf.options['default'] = True
        # conf.options['config_location'] = args['config']
        conf.options['display_options'] = args['display']
        conf.options['color'] = args['color']
        conf.options['clear_directory'] = args['clean']
        conf.options['interactive'] = args['interactive']
    else:
        # ! Weird
        raise Exception('Weird')
    return conf


def action_taker(args):
    conf = initialize(args)
    writers = [
        'git',
        'setup_py',
        'setup_cfg',
        'requirements',
        'license',
        'readme',
        'contributing',
        'manifest',
        'dockerfile',
        'gitignore',
        'tests']
    licenses = ['mit', 'agpl3', 'apache2', 'gnu2',
                'gnugpl3', 'gpl3', 'lgpl3', 'mpl2', 'unilicense']

    # ? Setting up of Variables and Preprocessing.
    if conf.options['license'].lower() in licenses:
        # print(f'License {conf.license}')
        pass
    else:
        raise NotImplementedError("This license is not yet implemented")

    if os.path.exists(os.path.join('.', conf.options['project_name'])):
        # the file is there
        pass
        # if conf.options['clear_directory'] is True:
        #     if os.path.exists(os.path.join('.', conf.options['project_name'])) is True:
        #         # Delete
        #         # os.rmdir(
        #         #     os.path.join('.', conf.options['project_name'])
        #         # )
        #         warnings.warn('Deleting the file inplace.')
        #         shutil.rmtree(
        #             os.path.join('.', conf.options['project_name'])
        #         )
        # else:
        #     # print(os.path.exists(os.path.join(
        #         # '.', conf.options['project_name'])))
        #     raise FileExistsError('A file with similar name exists')

    elif os.access(os.path.dirname(os.path.join('.', conf.options['project_name'])), os.W_OK):
        # the file does not exists but write privileges are given
        os.makedirs(os.path.join('.', conf.options['project_name']))
        # pass
    else:
        # can not write there
        raise PermissionError('Do not have the permission to Write here.')

        # else:
        #     # file doesn't exist. No need to bring in deletion.
        #     pass

    # ! Writing the files.
    if conf.options['config_location']:
        # Searching for the custom config thing.
        if not os.path.isfile(os.path.join(os.getcwd(), conf.options['config_location'])):
            raise FileNotFoundError(
                f"Cant find the config file {os.path.join(os.getcwd(), conf.options['config_location'])}")

    utils.writer_writer(conf)


def main():
    args = options()
    action_taker(args)


def run_as_command():
    main()


def questions():
    conf = Config()
    emojis = ['🚀', '✅', '🏠', '📘', '📦', '💡', '📝', '👤', '👤', '📃', '🗕', 'ℹ']
    answers = {}
    questions_to_ask = [
        ['    Project Name:  ', '', conf.options['project_name']],
        ['    Project Version:  ', '0.01', conf.options['project_version']],
        ['    Project Description:  ', '', conf.options['project_description']],
        ['    Author Name:  ', '', conf.options['author_name']],
        ['    Github Username:  ', '', conf.options['github_username']],
        ['    License Type:   ', 'mit', conf.options['license']],
        ['    Minimal Installation? (Y/N):   ', '',
         conf.options['default']],

        ['    Custom Config Location [Leave empty if not present]:  ',
            'config.yaml', conf.options['config_location']],
        ['    Github Email:  ', '', conf.options['author_email']],
        ['    Git Repository (Y/n): ', '', conf.options['files']['git']],
        ['    Contributing.md (Y/n): ', '',
         conf.options['files']['contributing']],
        ['    Setup.cfg (Y/n): ', '', conf.options['files']['setup_cfg']],
        ['    Tests folder (Y/n): ', 'yes', conf.options['files']['tests']],
        ['    Conda feed stock (Y/n): ', '', conf.options['files']['conda']],
        ['    Shields? (Y/n)  T: ', 'YES'],
        ['                    |-license  (Y/n): ',
         'mit', conf.options['shields']['base'].append('license')],
        ['                    |-Builds   (Y/n): ',
         'appveyor', conf.options['shields']['base'].append('license')],
        ['                    |-version  (Y/n): ',
         'pypi', conf.options['shields']['base'].append('license')],
        ['                    |-Issues   (Y/n): ',
         'github-issues', conf.options['shields']['base'].append('license')],
        ['                    |-PRs      (Y/n): ',
         'github-pull-requests', conf.options['shields']['base'].append('license')],
    ]
    for question, answer, something in questions_to_ask:
        answers[question] = str(
            utils.input_with_prefill(question, answer)).lower()

        if question == questions_to_ask[6][0] and answers[question] == 'y':
            break
    print(json.dumps(answers, indent=2))
    # print(json.dumps(conf.options, indent=2))
    print(
        '''
    ______________________________
    |                            |
    | Generation was successful  |
    | -------------------------  |
    | $ cd repo_name             |
    | $ python setup.py install  |
    ------------------------------
'''
    )


# questions()


def parser():
    raise NotImplementedError


def create_home_dir():
    """Create Directory for projectpy."""
    current_platform = platform.system().lower()
    if current_platform != 'windows':
        import pwd

    # create the necessary directory structure for storing config details
    # in the ~/.projectpy directory
    required_dirs = [os.path.join(HOME_DIR, dirs)
                     for dirs in ['', 'config', 'history']]
    for dir in required_dirs:
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
                if (current_platform != 'windows') and os.getenv("SUDO_USER"):
                    # owner of .projectpy should be user even when installing
                    # w/sudo
                    pw = pwd.getpwnam(os.getenv("SUDO_USER"))
                    os.chown(dir, pw.pw_uid, pw.pw_gid)
            except OSError:
                print("ProjectPy lacks permission to "
                      "access the ~/.projectpy/ directory.")
                raise
