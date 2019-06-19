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

    ap.add_argument("-n", "--name", required=True, help="Name of the project")

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
        print(json.dumps(utils.custom_reader(
            args['config']).options, indent=4))
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

        if conf.options['clear_directory'] is True:
            if os.path.exists(os.path.join('.', conf.options['project_name'])) is True:
                print('lololllloooo')
                # Delete
                # os.rmdir(
                #     os.path.join('.', conf.options['project_name'])
                # )
                warnings.warn('Deleting the file inplace.')
                shutil.rmtree(
                    os.path.join('.', conf.options['project_name'])
                )
        else:
            # print(os.path.exists(os.path.join(
                # '.', conf.options['project_name'])))
            raise FileExistsError('A file with similar name exists')

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
    print("The options chosen are as follows:")
    print(json.dumps(conf.options, sort_keys=True, indent=4))
    utils.writer_writer(conf)

    # if conf.default:
    #     for writes in conf.options['files'].keys():
    #         if writes == 'license' and conf.options['files'][writes]:
    #             conf.actions[writes](
    #                 f'./{conf.project_name}', conf.options['files']['license'])

    #         try:
    #             conf.actions[writes](
    #                 f'./{conf.project_name}')
    #         except BaseException:
    #             # warnings.warn('Some error occured, clearing the folder')
    #             # shutil.rmtree(
    #             #     os.path.join('.', conf.project_name)
    #             # )
    #             pass

    #         if writes == 'setup_py':
    #             conf.actions[writes](
    #                 f'./{conf.project_name}', conf.options)

    #         if writes == 'main':
    #             conf.actions[writes](
    #                 f'./{conf.project_name}', conf.options['project_name'])
    # try:
    # print(conf.options)
    # generate_README(os.path.join(
    #     '.', f'./{conf.project_name}'), shields=conf.options['shields'])

    # print(conf.basic)
    # except Exception as e:
    # print(e)
    # raise RuntimeError('There was a problem generating the README.md')


def main():
    args = options()
    action_taker(args)


def run_as_command():
    main()


def questions():
    answers = {}
    questions_to_ask = [
        'Project Name:',
        'Project Version:',
        'Project Description:',
        'Author Name:',
        'Github Username:',
        'License Type: ',
        'Minimal Installation? (Y/N): ',

        'Custom Config Location [Leave empty if not present]:'
    ]
    for question in questions_to_ask:
        answers[question] = str(input(question))

    print(answers)


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
