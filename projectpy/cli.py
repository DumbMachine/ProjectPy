import argparse
from . import utils
import sys


def options():
    '''
    Parsing the Arguments here
    '''
    ap = argparse.ArgumentParser(prog="projectpy",
                                usage="python3 %(prog)s [options]",
                                description="projectpy - A create-python-package CLI")

    ap.add_argument("-l", "--license", required=True, help="choice of LICENSE")
    ap.add_argument("-ig", "--gitignore", required=True,
                    help='''Language Choice for gitignore
                    {"python": To add Python .gitignore}
                        ''')

    ap.add_argument("-re", "--readme", required=True, help="Language Choice for gitignore")

    ap.add_argument("-co", "--contributing", required=True, help="Is contributing.rst required")

    ap.add_argument("-ci", "--cintergrations", required=True,
                    help='''Choice of the Continuous Integration\n
                    {
                        "travis": For the choice of using travis-ci,
                        "tox": For the choice of using Tox,
                        "jenkins": For the choice of using Jenkins
                            }''')

    ap.add_argument("-mi", "--manifest", required=True, help="Choice for the Manifest File")

    ap.add_argument("-d", "--docker", required=True, help="Choice for basic docker configuration with Alphine")

    ap.add_argument("-c", "--config", required=True, help="Display the Default Config")

    ap.add_argument("-noc", "--no-color", required=True, help="Do not emit color codes in output")

    ap.add_argument("-req", "--requriements.txt", required=True, help="Reqruiements to text")


    return vars(ap.parse_args())


def main():
    args = options()
    # print(args)
    utils.cprint("TICK", "Option", "Choice", heading=True)
    for key in args.keys():
        utils.cprint('[INFO]',key, args[key])

    print()


def run_as_command():
    version = ".".join(str(v) for v in sys.version_info[:2])
    if float(version) < 3.0:
        print("[-] TWINT requires Python version 3.6+.")
        sys.exit(0)

    main()