import argparse
from utils import cprint

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description="This is the small description things")

ap.add_argument("-l", "--license", required=True, help="choice of LICENSE")

ap.add_argument("-ig", "--gitignore", required=True, help="Language Choice for gitignore")

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

ap.add_argument("-d", "--doccker", required=True, help="Choice for basic docker configuration with Alphine")

ap.add_argument("-c", "--config", required=True, help="Display the Default Config")

ap.add_argument("-noc", "--no-color", required=True, help="Do not emit color codes in output")


args = vars(ap.parse_args())


cprint("TICK", "Option", "Choice", heading=True)
for key in args.keys():
    cprint('[INFO]',key, args[key])

print()