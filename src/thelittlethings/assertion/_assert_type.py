from typing import Iterable


def assert_type(obj, type):
    if not isinstance(obj, type):
        if isinstance(type, Iterable):
            if len(type) > 0:
                type_str = type[-1].__name__
            if len(type) > 1:
                type_str = type[-2].__name__ + " or " + type_str
            for i in range(3, len(type) + 1):
                type_str = type[-i].__name__ + ", " + type_str
        else:
            type_str = type.__name__
        raise AssertionError(f"Object is not an instance of {type_str}.")


assert_type(1, (bool))