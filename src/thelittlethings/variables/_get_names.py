import inspect
from typing import List


def get_names(var) -> List[str]:
    """
    retrieve all names of a variable in the current frame
    """

    frame = inspect.currentframe().f_back
    # Combine global and local variable dicts
    var_dict = frame.f_globals.copy()
    var_dict.update(frame.f_locals)
    return [name for name, value in var_dict.items() if value is var]
