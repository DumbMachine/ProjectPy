import argparse
import os
import sys

from . import config, utils
import site

from colorama import Fore, init

init(autoreset=True)

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
    
    ap.add_argument("-c", "--custom", required=False, help="Take the customs we provide", default='unilicense')
    
    ap.add_argument("-ci", "--cintergrations", required=False,
                    help='''Choice of the Continuous Integration\n
                    {
                        "travis": For the choice of using travis-ci,
                        "tox": For the choice of using Tox,
                        "jenkins": For the choice of using Jenkins
                            }''', default='travis')

    ap.add_argument("-con", "--config", required=False, help="Display the Default Config", default=True)

    ap.add_argument("-noc", "--color", required=False, help="Do not emit color codes in output", default=False)
        
    ap.add_argument("-clr", "--clean", required=False, help="Delete the folder, if similar exists", default=False)
    
    ap.add_argument("-custom", "--git", required=False, help="Delete the folder, if similar exists", default=False)


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
    
    conf.docker = args.docker
    conf.color = args.color
    conf.ci = args.cintergrations
    conf.license = args.license
    conf.clear = args.clear
    return conf

def main():
    args = options()
    # print(Fore.GREEN,args)
    
    if os.path.exists(os.path.join(os.getcwd(),args['name'])):
        raise FileExistsError((Fore.RED + "The file exitsts already. Pass -clr, if you want to delete that folder"))            
        
    else:
        os.makedirs(os.path.join(os.getcwd(), args['name']))
        
    # ! Compying the contents of template to Target
    from distutils.sysconfig import get_python_lib
    files_to_copy = utils.files()
    for file in files_to_copy:
        location = os.path.join(get_python_lib(),'projectpy/template',file)
        utils.copy_files(location,  args['name'])
    # utils.copy_files(os.path.join(get_python_lib(),'projectpy/template'), args['name'])
    # utils.cprint("TICK", "Option", "Choice", heading=True)
    # for key in args.keys():
    #     utils.cprint('[INFO]',key, args[key])

    # print()
    # conf = initialize(options())
    
    # if conf.usermail == True:
    #     conf.git = True
    


def parser(conf):
    pass
    #username
    

def run_as_command():
    main()
