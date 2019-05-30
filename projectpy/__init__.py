import platform
from pathlib import Path
import os
from . import utils


home = str(Path.home())
app_data = ".create-python-package"
if os.path.exists(os.path.join(home,app_data)):
    os.system("rm -r {}".format(os.path.join(home,app_data)))
    print("something")
else:
    os.makedirs(os.path.join(home,app_data))
    print("sometingelse")
    
    
# utils.cprint("asdasdas ", "A create-python-package CLI", "", normal=True)