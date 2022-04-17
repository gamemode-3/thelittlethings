from typing import Iterable


def assert_true(condition, error_message_appendix=None):
    if condition:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"condition is False{error_message_appendix}")

def assert_false(condition, error_message_appendix=None):
    if not condition:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"condition is True{error_message_appendix}")

def assert_equal(a, b, error_message_appendix=None):
    if a == b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} != {b}{error_message_appendix}")

def assert_not_equal(a, b, error_message_appendix=None):
    if a != b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} == {b}{error_message_appendix}")

def assert_is(a, b, error_message_appendix=None):
    if a is b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} is not {b}{error_message_appendix}")

def assert_greater(a, b, error_message_appendix=None):
    if a > b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} <= {b}{error_message_appendix}")

def assert_greater_equal(a, b, error_message_appendix=None):
    if a >= b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} < {b}{error_message_appendix}")

def assert_less(a, b, error_message_appendix=None):
    if a < b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} >= {b}{error_message_appendix}")

def assert_less_equal(a, b, error_message_appendix=None):
    if a <= b:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} > {b}{error_message_appendix}")

def assert_close(a, b, epsilon=1e-6, error_message_appendix=None):
    if abs(a - b) < epsilon:
        return True
    else:
        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"{a} != {b}{error_message_appendix}")

def assert_type(obj, type, error_message_appendix=None):
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

        if error_message_appendix is None:
            error_message_appendix = ""
        else:
            error_message_appendix = f": {error_message_appendix}"
        raise AssertionError(f"object is not an instance of {type_str}{error_message_appendix}")
    return True

def assert_types(objects, types, error_message_appendix=None):
    for index, obj, type in enumerate(zip(objects, types)):
        try:
            assert_type(obj, type)
        except AssertionError as e:
            if isinstance(type, Iterable):
                if len(type) > 0:
                    type_str = type[-1].__name__
                if len(type) > 1:
                    type_str = type[-2].__name__ + " or " + type_str
                for i in range(3, len(type) + 1):
                    type_str = type[-i].__name__ + ", " + type_str
            else:
                type_str = type.__name__
                
            if error_message_appendix is None:
                error_message_appendix = ""
            else:
                error_message_appendix = f": {error_message_appendix}"
            raise AssertionError(
                f"object number {index + 1} is not an instance of {type_str}{error_message_appendix}"
            ) from e
    return True
