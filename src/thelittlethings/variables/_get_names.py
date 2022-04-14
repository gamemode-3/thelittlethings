import inspect
from typing import List

# Retrieves all names of a variable
def get_names(var) -> List[str]:
    """
    Retrieves all names of a variable in the parent frame
    """
    frame = inspect.currentframe().f_back
    # Combine global and local variable dicts
    var_dict = frame.f_globals.copy()
    var_dict.update(frame.f_locals)
    return [name for name, value in var_dict.items() if value is var]