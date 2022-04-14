"""
## the little things
A library that provides a number of utilities to make your developement life easier.
"""

from .progress_bar import *
from . import auto_reload
from .mutable import *
from .variables import *
from .linked_values import *
from .testing import *
from .debug import *
from .extended_list import EList
from .values import *

import atexit

def reset_styles():
    import sys

    if not translate_color_codes(Log._full_str).endswith("\n"):
        sys.stdout.write("\n")
    sys.stdout.write(translate_color_codes("[Style: reset_all]\r"))
    sys.stdout.flush()
    
    Log.close_file()

atexit.register(reset_styles)
del atexit
