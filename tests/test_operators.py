import random
from src.thelittlethings import multi_test, assert_close, assert_equal
from src.thelittlethings.linked_values import *
from . import all_tests


def test_int_operators(operator: str):
    literal_a = random.randint(1, 20)
    literal_b = random.randint(1, 20)


    var_a = Var(literal_a)
    var_b = Var(literal_b)

    literal_c = eval(f"a {operator} b", {'a': literal_a, 'b': literal_b})
    var_c = eval(f"a {operator} b", {'a': var_a, 'b': var_b})

    assert_close(literal_c, var_c.value, error_message_appendix=f"failed on {literal_a} {operator} {literal_b}")
    return f"passed on {literal_a} {operator} {literal_b}"

def test_float_operators(operator: str):
    literal_a = random.random() * 19 + 1
    literal_b = random.random() * 19 + 1


    var_a = Var(literal_a)
    var_b = Var(literal_b)

    literal_c = eval(f"a {operator} b", {'a': literal_a, 'b': literal_b})
    var_c = eval(f"a {operator} b", {'a': var_a, 'b': var_b})

    if any(isinstance(x, (bool)) for x in [literal_a, literal_b]):
        assert_equal(literal_c, var_c.value, error_message_appendix=f"failed on {literal_a} {operator} {literal_b}")
    elif any(isinstance(x, (int, float)) for x in [literal_a, literal_b]):
        assert_close(literal_c, var_c.value, error_message_appendix=f"failed on {literal_a} {operator} {literal_b}")
    return f"passed on {literal_a} {operator} {literal_b}"

number_operators = ["+", "-", "*", "/", "**", "%", ">" ,"<", ">=", "<=", "==", "!="]


def test_bool_operators(operator: str):
    literal_a = bool(random.randint(0, 1))
    literal_b = bool(random.randint(0, 1))


    var_a = Var(literal_a)
    var_b = Var(literal_b)

    literal_c = eval(f"a {operator} b", {'a': literal_a, 'b': literal_b})
    var_c = eval(f"a {operator} b", {'a': var_a, 'b': var_b})

    assert_equal(literal_c, var_c.value, error_message_appendix=f"failed on {literal_a} {operator} {literal_b}")
    return f"passed on {literal_a} {operator} {literal_b}"

boolean_operators = ["&", "|", "^"]

all_tests.all_tests.append(
    (number_operators, test_int_operators, test_float_operators, {"iterations": 100})
)
all_tests.all_tests.append(
    (boolean_operators, test_bool_operators, {"iterations": 100})
)