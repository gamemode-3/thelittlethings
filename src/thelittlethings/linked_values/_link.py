from typing import Any, Tuple, Type, TypeVar
from ..mutable._mutable import Mutable
from ._operators import *
from inspect import signature
from ..assertion import assert_type, assert_true


T = TypeVar("T")


class Link(Mutable[T]):
    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return RSub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)

    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return RDiv(self, other)

    def __pow__(self, other):
        return Pow(self, other)

    def __rpow__(self, other):
        return RPow(self, other)

    def __mod__(self, other):
        return Mod(self, other)

    def __rmod__(self, other):
        return Mod(other, self)

    def __abs__(self):
        return Abs(self)

    def __neg__(self):
        return Mul(self, -1)

    def __invert__(self):
        return Not(self)

    def __eq__(self, other):
        return Eq(self, other)

    def __ne__(self, other):
        return Ne(self, other)

    def __gt__(self, other):
        return Gt(self, other)

    def __ge__(self, other):
        return Ge(self, other)

    def __lt__(self, other):
        return Lt(self, other)

    def __le__(self, other):
        return Le(self, other)

    def __and__(self, other):
        return And(self, other)

    def __rand__(self, other):
        return And(other, self)

    def __or__(self, other):
        return Or(self, other)

    def __ror__(self, other):
        return Or(other, self)

    def __xor__(self, other):
        return Xor(self, other)

    def __rxor__(self, other):
        return Xor(other, self)

    def __iadd__(self, other):
        other_value = other.value if isinstance(other, OperatorLink) else other
        self.value += other_value
        return self


class Attr(Link[T]):
    def __init__(self, obj: Any, attr: str, type_hint: Type[T] = Any, immutable=False):
        self.obj = obj
        self.attr = attr
        self.immutable = immutable

    @property
    def value(self) -> T:
        return getattr(self.obj, self.attr)

    @value.setter
    def value(self, value: T):
        if self.immutable:
            raise AttributeError(
                "attribute is immutable. modify it using set_value(value)."
            )
        setattr(self.obj, self.attr, value)

    def set_value(self, value: T):
        setattr(self.obj, self.attr, value)


class Var(Link[T]):
    def __init__(self, value: T, immutable=False):
        self._value = value
        self.immutable = immutable

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        if self.immutable:
            raise AttributeError(
                "variable is immutable. modify it using set_value(value)."
            )
        self._value = value

    def set_value(self, value: T):
        self._value = value


class OperatorLink(Link[T]):
    def __init__(self, operator: Type[Operator], *values: "Tuple[T, ...]"):
        assert_type(operator, Type[Operator])
        assert_type(
            values[0],
            Mutable,
            f"the first input to an OperatorLink like {self.__class__.__name__} must be a Mutable. use Var(value) to create one.",
        )

        self.operator: Type[Operator] = operator
        self.inputs = list(values)

        values_given = len(values)
        values_expected = signature(operator._eval).parameters.__len__()
        if values_given != values_expected:
            for attr in signature(operator._eval).parameters.values():
                # If an unpack operation is used, the given arguments will not exceed the expected arguments.
                if str(attr).startswith("*") and not str(attr).startswith("**"):
                    break
            else:
                raise ValueError(
                    f"wrong number of values for {operator.__name__} (expected {values_expected}, got {values_given})"
                )

        self.order = operator.order
        self.print_pattern = operator.print_pattern

    @property
    def value(self) -> T:
        inputs = (
            value.value if isinstance(value, Mutable) else value
            for value in self.inputs
        )

        return self.operator(*inputs)

    @value.setter
    def value(self, value):
        # Modify the first value using the reverse operation
        try:
            value1 = self.operator.reverse(value, *self.inputs[1:])
            if value1 is not None:
                if isinstance(self.inputs[0], Mutable):
                    self.inputs[0].__set__(self, value1)
                else:
                    self.inputs[0] = value1
            else:
                raise ValueError(
                    f"value cannot be set: {self.operator.__name__}({self.inputs[0]}, <Any>) != {value}"
                )
        except NotImplementedError as e:
            print(e.with_traceback())
            print("cannot set value for link without reverse operation")

    def __repr__(self):
        # return the link string using the print pattern
        return_value = self.print_pattern
        operator_inputs = signature(self.operator._eval).parameters

        for index, (value, name) in enumerate(zip(self.inputs, operator_inputs)):

            def is_paren_needed(value):
                if len(operator_inputs) <= 1:
                    return False
                if isinstance(value, OperatorLink):
                    if value.order < self.order:
                        return True
                    if (
                        index != 0
                        and value.order == self.order
                        and value.operator.__name__ != self.operator.__name__
                    ):
                        return True

            if is_paren_needed(value):
                value = f"({repr(value)})"

            else:
                value = repr(value)

            return_value = return_value.replace(f"${name}", value)

        return return_value

    def __getitem__(self, key):
        return self.inputs[key]

    def __setitem__(self, key, value):
        self.inputs[key] = value


class Eq(OperatorLink[bool]):
    def __init__(self, a: OperatorLink, b: OperatorLink):
        super().__init__(EqualOperator, a, b)


class Ne(OperatorLink[bool]):
    def __init__(self, a: OperatorLink, b: OperatorLink):
        super().__init__(NotEqualOperator, a, b)


class Gt(OperatorLink[bool]):
    def __init__(self, a: OperatorLink, b: OperatorLink):
        super().__init__(GreaterOperator, a, b)


class Ge(OperatorLink[bool]):
    def __init__(self, a: OperatorLink, b: OperatorLink):
        super().__init__(GreaterEqualOperator, a, b)


class Lt(OperatorLink[bool]):
    def __init__(self, a: OperatorLink, b: OperatorLink):
        super().__init__(LessOperator, a, b)


class Le(OperatorLink[bool]):
    def __init__(self, a: OperatorLink, b: OperatorLink):
        super().__init__(LessEqualOperator, a, b)


class NumberOperatorLink(OperatorLink[T]):
    pass


class Add(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(AdditionOperator, a, b)


class Sub(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(SubtractionOperator, a, b)


class RSub(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(BackwardsSubtractionOperator, a, b)


class Mul(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(MultiplicationOperator, a, b)


class Div(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(DivisionOperator, a, b)


class RDiv(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(BackwardsDivisionOperator, a, b)


class Pow(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(PowerOperator, a, b)


class RPow(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(BackwardsPowerOperator, a, b)


class Root(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(RootOperator, a, b)


class RRoot(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(BackwardsRootOperator, a, b)


class Mod(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(ModuloOperator, a, b)


class Abs(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T"):
        super().__init__(AbsoluteOperator, a)


class Ln(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T"):
        super().__init__(NaturalLogarithmOperator, a)


class LogB(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(BaseBLogarithmOperator, a, b)


class RLogB(NumberOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(BackwardsBaseBLogarithmOperator, a, b)


class BooleanOperatorLink(OperatorLink[T]):
    pass


class And(BooleanOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(AndOperator, a, b)


class Or(BooleanOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(OrOperator, a, b)


class Xor(BooleanOperatorLink[T]):
    def __init__(self, a: "Link[T] | T", b: "Link[T] | T"):
        super().__init__(XorOperator, a, b)


class Not(BooleanOperatorLink[T]):
    def __init__(self, a: "Link[T] | T"):
        super().__init__(NotOperator, a)
