import argparse
from . import utils
import sys
import os

def options():
    '''
    Parsing the Arguments here
    '''
    ap = argparse.ArgumentParser(prog="projectpy",
                                usage="%(prog)s [options]",
                                description="projectpy - A create-python-package CLI")

    ap.add_argument("-l", "--license", required=False, help="choice of LICENSE")
    ap.add_argument("-ig", "--gitignore", required=False,
                    help='''Language Choice for gitignore
                    {"python": To add Python .gitignore}
                        ''')

    ap.add_argument("-re", "--readme", required=False, help="Language Choice for gitignore")

    ap.add_argument("-co", "--contributing", required=False, help="Is contributing.rst required")

    ap.add_argument("-ci", "--cintergrations", required=False,
                    help='''Choice of the Continuous Integration\n
                    {
                        "travis": For the choice of using travis-ci,
                        "tox": For the choice of using Tox,
                        "jenkins": For the choice of using Jenkins
                            }''')

    ap.add_argument("-mi", "--manifest", required=False, help="Choice for the Manifest File")

    ap.add_argument("-d", "--docker", required=False, help="Choice for basic docker configuration with Alphine")

    ap.add_argument("-c", "--config", required=False, help="Display the Default Config")

    ap.add_argument("-noc", "--no-color", required=False, help="Do not emit color codes in output")

    ap.add_argument("-req", "--requriements.txt", required=False, help="Reqruiements to text")
    
    ap.add_argument("-n", "--name", required=True, help="Name of the project")



    return vars(ap.parse_args())


def main():
    args = options()
    # print(args)
    os.makedirs(os.path.join(os.getcwd(),args['name']))
    os.system('echo "GAYSHIT" ./name/something.txt')
    utils.cprint("TICK", "Option", "Choice", heading=True)
    for key in args.keys():
        utils.cprint('[INFO]',key, args[key])

    print()


def run_as_command():
    main()