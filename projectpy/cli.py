from . import config, utils
from colorama import Fore, init
import argparse
import os
import site
import sys
import textwrap
import time
from .writer import *
import shutil
from .generator import generate_README
import warnings

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
    conf.project_name = args['name']
    conf.default = args['default']
    conf.default = True
    conf.config_location = args['config']
    if args['config']:
        conf.default = False
    conf.display_options = args['display']
    conf.color = args['color']
    conf.clear_directory = args['clean']
    conf.interactive = args['interactive']

    return conf


def main():
    args = options()
    action_taker(initialize(args))


def action_taker(conf):
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
    if conf.license.lower() in licenses:
        # print(f'License {conf.license}')
        pass
    else:
        raise NotImplementedError("This license is not yet implemented")

    if os.path.exists(os.path.join('.', conf.project_name)):
        # the file is there
        raise FileExistsError('A file with similar name exists')
    elif os.access(os.path.dirname(os.path.join('.', conf.project_name)), os.W_OK):
        # the file does not exists but write privileges are given
        os.makedirs(os.path.join('.', conf.project_name))
        # pass
    else:
        # can not write there
        raise PermissionError('Do not have the permission to Write here.')

    if conf.clear_directory:
        if os.path.exists(os.path.join('.', conf.project_name)):
            # Delete
            # os.rmdir(
            #     os.path.join('.', conf.project_name)
            # )
            shutil.rmtree(
                os.path.join('.', conf.project_name)
            )
        else:
            # file doesn't exist. No need to bring in deletion.
            pass

    # ! Writing the files.
    if not conf.default:
        # Searching for the custom config thing.
        # if os.path.isfile(os.path.join(conf.config_location, '.config.yaml')):
        import yaml
        thing = yaml.load(
            open(
                os.path.join(
                    conf.config_location
                    # '.'
                    # '.config.yaml'
                )
            ),
            Loader=yaml.Loader)
        # print(configuration)
        conf = config.Config()
        for item in thing.keys():
            if item in utils.files:
                conf.all['files'][item] = thing[item]
            elif item in utils.shields:
                conf.all['shields']['base'].append(item)
                conf.all['shields']['entity'].append(thing[item])
            else:
                # try:
                conf.all[item] = thing[item]

        for writes in conf.all['files'].keys():
            if writes == 'license':
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}', conf.all['files']['license'])

            try:
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}')
            except BaseException:
                warnings.warn('Some error occured, clearing the folder')
                shutil.rmtree(
                    os.path.join('.', conf.project_name)
                )
                # pass

            if writes == 'setup_py':
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}', conf.all)

            if writes == 'main':
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}', conf.all['project_name'])
        # try:
            generate_README(os.path.join(
                f'./{conf.project_name}'), shields=conf.basic['shields'])
        else:
            raise FileNotFoundError(
                'config.yaml was not found in the mentioned directory.')
        # Reading the custom config thing.

        # Writing by respecting the config.yml.
        # raise NotImplementedError

    if conf.default:
        for writes in conf.basic['files'].keys():
            if writes == 'license':
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}', conf.basic['files']['license'])

            try:
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}')
            except BaseException:
                # warnings.warn('Some error occured, clearing the folder')
                # shutil.rmtree(
                #     os.path.join('.', conf.project_name)
                # )
                pass

            if writes == 'setup_py':
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}', conf.basic)

            if writes == 'main':
                conf.actions['default']['files'][writes](
                    f'./{conf.project_name}', conf.basic['project_name'])
        # try:
        generate_README(os.path.join(
            '.', f'./{conf.project_name}'), shields=conf.basic['shields'])

        # print(conf.basic)
        # except Exception as e:
        # print(e)
        # raise RuntimeError('There was a problem generating the README.md')


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
    """Create Directory for retriever."""
    current_platform = platform.system().lower()
    if current_platform != 'windows':
        import pwd

    # create the necessary directory structure for storing scripts/raw_data
    # in the ~/.retriever directory
    required_dirs = [os.path.join(HOME_DIR, dirs)
                     for dirs in ['', 'config', 'history']]
    for dir in required_dirs:
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
                if (current_platform != 'windows') and os.getenv("SUDO_USER"):
                    # owner of .retriever should be user even when installing
                    # w/sudo
                    pw = pwd.getpwnam(os.getenv("SUDO_USER"))
                    os.chown(dir, pw.pw_uid, pw.pw_gid)
            except OSError:
                print("ProjectPy lacks permission to "
                      "access the ~/.projectpy/ directory.")
                raise
