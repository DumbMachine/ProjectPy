from . import config, utils
from colorama import Fore, init
import argparse
import os
import site
import sys
import textwrap
import time
from distutils.sysconfig import get_python_lib
from .writer import *
import shutil

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

    # ap.add_argument(
    #     "-us",
    #     "--username",
    #     required=False,
    #     help="Github Username",
    #     default=" username")
    # ap.add_argument(
    #     "-ue",
    #     "--usermail",
    #     required=False,
    #     help="Email of the User",
    #     default=' usermail')

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
    conf.config_location = args['config']
    conf.display_options = args['display']
    conf.color = args['color']
    conf.clear_directory = args['clean']
    conf.interactive = args['interactive']

    # conf.username = args.username
    # conf.usermail = args.usermail

    # # conf.docker = args.docker
    # conf.color = args.color
    # # conf.ci = args.cintergrations
    # # conf.license = args.license
    # conf.clear = args.clear
    # conf.interactive = args.interactive

    return conf


def main():
    args = options()
    # print(f'OPTIONS {args}')
    # print(args['name'])
    # print(f'CONFIG {initialize(args)}')
    # print(Fore.GREEN, args)

    # if os.path.exists(os.path.join(os.getcwd(), args['name'])):
    #     raise FileExistsError(
    #         (Fore.RED +
    #          "The file exitsts already. Pass -clr, if you want to delete that folder"))

    # else:
    #     os.makedirs(os.path.join(os.getcwd(), args['name']))

    # # ! Compying the contents of template to Target
    # try:
    #     import site
    #     base = site.getsitepackages()[0]
    # except BaseException:
    #     base = get_python_lib()
    # files_to_copy = utils.files()
    # i = 0
    # for file in files_to_copy:
    #     location = os.path.join(base, 'projectpy/template', file)
    #     utils.copy_files(location, args['name'])
    #     time.sleep(0.001)
    #     utils.progressBar(i *
    #                       len(files_to_copy), len(files_to_copy) *
    #                       10, "Copying file {}".format(file[:15]))
    #     i += 1

    # print()

    # print(utils.replacer(args['name']))
    # utils.cprint(os.getcwd(), "", "")
    # utils.cprint("TICK", "Option", "Choice", heading=True)
    # for key in args.keys():
    #     utils.cprint('[INFO]', key, args[key])

    print("Creating the new folder")

    action_taker(initialize(args))
    print(initialize(args).license)
    # conf = initialize(options())

    # if conf.usermail == True:
    #     conf.git = True


def action_taker(conf):
    writers = ['git', 'setup_py', 'setup_cfg', 'requirements', 'license', 'readme', 'contributing',
               'manifest', 'dockerfile', 'gitignore']
    licenses = ['mit', 'agpl3', 'apache2', 'gnu2',
                'gnugpl3', 'gpl3', 'lgpl3', 'mpl2', 'unilicense']

    if conf.license.lower() in licenses:
        print(f'License {conf.license}')
    else:
        raise NotImplementedError("This license is not yet implemented")

    if os.path.exists(conf.config_location):
        # the file is there
        raise FileExistsError('A file with similar name exists')
    elif os.access(os.path.dirname(conf.config_location), os.W_OK):
        # the file does not exists but write privileges are given
        pass
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
    for writes in writers:
        if conf.writes:


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
