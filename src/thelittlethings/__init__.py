"""
## the little things
a library full of small utilities for you to use in your code
"""

from .progress_bar import *
from . import auto_reload
from .assertion import *
from .mutable import *
from .variables import *
from .linked_values import *
from .testing import *
from .debug import *
from .extended_list import EList
from .constants import *
from .testing import *
from . import to_string

import atexit

def reset_styles():
    import sys

    try:
        if not translate_color_codes(Log._full_str, console=False).endswith("\n"):
            sys.stdout.write("\n")
    except SyntaxError:
        pass
    sys.stdout.write(translate_color_codes("[style: reset_all]\r"))
    sys.stdout.flush()
    
    Log.close_file()

atexit.register(reset_styles)
del atexit
