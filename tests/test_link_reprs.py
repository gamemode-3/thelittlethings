from src.thelittlethings import test, assert_close
from src.thelittlethings.linked_values import *


def test_link_repr(link: Link):
    """
    test whether the repr of a link is correct
    """
    link_repr = repr(link)
    repr_eval: Link = eval(link_repr, globals())

    assert_close(link.value, repr_eval.value)


links = [
    Var(1) + 2 + 3,
    Var(1) + 2 + 3 + 4,
    Var(2) + 3 / 4,
    3 / 4 + Var(2),
    3 + 4 / Var(2),
    3 + 4 / Var(2) + 5,
    (3 + 4) / Var(2) + 5,
    (3 + 4) / (Var(2) + 5),
    3 % Var(2) + 5,
    Var(2) % 3 + 5,
]

test(links, test_link_repr)