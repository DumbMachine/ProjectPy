import argparse
# from . import utils
import sys

def options():
    '''
    Parsing the Arguments here
    '''
    ap = argparse.ArgumentParser(prog="projectpy",
                                usage="%(prog)s [options]",
                                description="projectpy - A create-python-package CLI")

    ap.add_argument("-l", "--license", required=True, help="choice of LICENSE")
    ap.add_argument("-re", "--requirements.txt", required=False, nargs='+', help="choice of LICENSE")


    return vars(ap.parse_args())


def main():
    args = options()
    # print(args)
    utils.cprint("TICK", "Option", "Choice", heading=True)
    for key in args.keys():
        utils.cprint('[INFO]',key, args[key])

    print()


def run_as_command():
    main()