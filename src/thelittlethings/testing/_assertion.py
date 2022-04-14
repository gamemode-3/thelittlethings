from typing import Iterable


def assert_true(condition):
    if condition:
        return True
    else:
        raise AssertionError("Condition is False")

def assert_false(condition):
    if not condition:
        return True
    else:
        raise AssertionError("Condition is True")

def assert_equal(a, b):
    if a == b:
        return True
    else:
        raise AssertionError(f"{a} != {b}")

def assert_not_equal(a, b):
    if a != b:
        return True
    else:
        raise AssertionError(f"{a} == {b}")

def assert_is(a, b):
    if a is b:
        return True
    else:
        raise AssertionError(f"{a} is not {b}")

def assert_greater(a, b):
    if a > b:
        return True
    else:
        raise AssertionError(f"{a} <= {b}")

def assert_greater_equal(a, b):
    if a >= b:
        return True
    else:
        raise AssertionError(f"{a} < {b}")

def assert_less(a, b):
    if a < b:
        return True
    else:
        raise AssertionError(f"{a} >= {b}")

def assert_less_equal(a, b):
    if a <= b:
        return True
    else:
        raise AssertionError(f"{a} > {b}")

def assert_close(a, b, epsilon=1e-6):
    if abs(a - b) < epsilon:
        return True
    else:
        raise AssertionError(f"{a} != {b}")

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


del Iterable