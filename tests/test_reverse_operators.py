import inspect
import random
from typing import Type
from src.thelittlethings import test, assert_close, Var, NumberOperatorLink, get_all_subclasses
from . import all_tests


def test_reverse_operators(operator: Type[NumberOperatorLink]):
    value_a = random.random() * 19 + 1
    value_b = random.random() * 19 + 1

    var_a = Var(value_a)
    var_b = Var(value_b)

    var_c = operator(var_a, var_b)

    target = random.random() * 19 + 1
    var_c.value = target

    assert_close(target, var_c.value, error_message_appendix=f"failed on {operator.__name__}({value_a: .2f}, {value_b: .2f}) -> {operator.__name__}({float(var_a.value): .2f}, {float(var_b.value): .2f})")


operators = [
    op for op in get_all_subclasses(NumberOperatorLink)
    if op(*(1 for _ in range(len(inspect.signature(op.__init__).parameters) - 1))).operator.has_reverse()
    and len(inspect.signature(op.__init__).parameters) == 3
]

all_tests.all_tests.append((operators, test_reverse_operators, {"iterations": 100}))