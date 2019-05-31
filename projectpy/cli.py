import argparse
import os
import sys

from . import config, utils
import site


def options():
    '''
    Parsing the Arguments here
    '''
    ap = argparse.ArgumentParser(prog="projectpy",
                                usage="%(prog)s [options]",
                                description="projectpy - A create-python-package CLI")

    ap.add_argument("-n", "--name", required=True, help="Name of the project")
    ap.add_argument("-us", "--username", required=False, help="Github Username", default=" username")
    ap.add_argument("-ue", "--usermail", required=False, help="Email of the User", default=' usermail')
    
    ap.add_argument("-l", "--license", required=False, help="choice of LICENSE", default='unilicense')
    ap.add_argument("-ig", "--gitignore", required=False, help='Language Choice for gitignore', default=True)

    ap.add_argument("-re", "--readme", required=False, help="Language Choice for gitignore", default=True)

    ap.add_argument("-co", "--contributing", required=False, help="Is contributing.rst required", default=False)

    ap.add_argument("-ci", "--cintergrations", required=False,
                    help='''Choice of the Continuous Integration\n
                    {
                        "travis": For the choice of using travis-ci,
                        "tox": For the choice of using Tox,
                        "jenkins": For the choice of using Jenkins
                            }''', default='travis')

    ap.add_argument("-mi", "--manifest", required=False, help="Choice for the Manifest File", default=True)

    ap.add_argument("-d", "--docker", required=False, help="Choice for basic docker configuration with Alphine", default=True)

    ap.add_argument("-c", "--config", required=False, help="Display the Default Config", default=True)

    ap.add_argument("-noc", "--no-color", required=False, help="Do not emit color codes in output", default=False)

    ap.add_argument("-req", "--requirements", required=False, help="Reqruiements to text", default=True)
        
    ap.add_argument("-clr", "--clear", required=False, help="Delete the folder, if similar exists", default=False)


    return vars(ap.parse_args())


def initialize(args):
    '''
    Sets the Config for the installation
    
    @params:
        args: argparse.ArguementParser
            : The arguments parsed by the CLI
    '''
    conf  = config.Config()
    conf.username = args.username
    conf.usermail = args.usermail
    
    conf.git = args.git
    conf.docker = args.docker
    conf.color = args.color
    conf.requirements = args.requirements
    conf.manifest = args.manifest
    conf.ci = args.cintergrations
    conf.readme = args.readme
    conf.license = args.license
    conf.gitignore = args.gitignore
    conf.contributing = args.contributing
    conf.clear = args.clear
    return conf

def main():
    args = options()
    if os.path.exists(os.path.join(os.getcwd(),args['name'])):
        raise FileExistsError("The file exitsts already. Pass -clr, if you want to delete that folder")
    else:
        os.makedirs(os.path.join(os.getcwd(), args['name']))
        
    # ! Compying the contents of template to Target
    from distutils.sysconfig import get_python_lib
    utils.copy_files(os.path.join(get_python_lib(),'projectpy/template'), args['name'])
    utils.cprint("TICK", "Option", "Choice", heading=True)
    for key in args.keys():
        utils.cprint('[INFO]',key, args[key])

    print()


def run_as_command():
    main()
