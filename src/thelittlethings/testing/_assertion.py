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