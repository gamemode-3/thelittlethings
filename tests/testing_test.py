from random import random, randrange
from thelittlethings import testing, get_all_subclasses, NumberOperator, Log


def test_reverse_operation_on_floats(operation, index):
    a = random() * 200 + 0
    b = random() * 20 + 1e-10
    try:
        c = operation(a, b)
        a_ = operation.reverse(c, b)
    except Exception as e:
        raise type(e)(f"Failed on [Style: bright]{a}[Style: reset_all] and [Style: bright]{b}[Style: reset_all]: {str(e)}") from e

    if testing.assert_close(a, a_):
        return f"Passed on [Style: bright]{a}[Style: reset_all] and [Style: bright]{b}[Style: reset_all]"

def test_reverse_operation_on_integers(operation):
    a = randrange(0, 200)
    b = randrange(1, 20)
    try:
        c = operation(a, b)
        a_ = operation.reverse(c, b)
    except Exception as e:
        raise type(e)(f"Failed on [Style: bright]{a}[Style: reset_all] and [Style: bright]{b}[Style: reset_all]: {str(e)}") from e

    if testing.assert_close(a, a_):
        return f"Passed on [Style: bright]{a}[Style: reset_all] and [Style: bright]{b}[Style: reset_all]"

Log.load_file("test.log")

testing.test(
    [
        operation
        for operation in get_all_subclasses(NumberOperator)
        if operation.has_reverse()
    ],
    test_reverse_operation_on_floats,
    test_reverse_operation_on_integers,
    iterations=10
)
