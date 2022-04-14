import os
from typing import Any
from ..values import UNDEFINED


def load_file(file_path: str, create_if_nonexistant=True, default: Any = UNDEFINED):
    if not isinstance(file_path, str):
        if default is UNDEFINED:
            raise TypeError("file_path must be a string")
        return default
    if create_if_nonexistant and not os.path.exists(file_path):
        return open(file_path, "x")
    else:
        return open(file_path, "w")