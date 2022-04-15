import os
from typing import Any
from ..constants import UNDEFINED


def load_file(file_path: str, create_if_nonexistant=True, default: Any = UNDEFINED):
    if not isinstance(file_path, str):
        if default is UNDEFINED:
            raise TypeError("file_path must be a string")
        return default
    if create_if_nonexistant and not os.path.exists(file_path):
        return open(file_path, "x")
    else:
        try:
            return open(file_path, "w")
        except FileNotFoundError as e:
            if default is UNDEFINED:
                raise e
            return default