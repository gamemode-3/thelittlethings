from typing import Any, Tuple, Type
from ..mutable._mutable import Mutable
from ._link_operation import Operation
from inspect import signature


class Link(Mutable):
    def __init__(self, operation: Type[Operation], *values: "Tuple[Mutable | Any, ...]"):
        assert issubclass(operation, Operation)
        self.operation = operation
        self.values = values

        values_given = len(values)
        values_expected = signature(operation).parameters.__len__()
        if values_given != values_expected:
            for attr in signature(operation).parameters.values():
                # If an unpack operation is used, the given arguments will not exceed the expected arguments.
                if str(attr).startswith("*") and not str(attr).startswith("**"):
                    break
            else:
                raise ValueError(f"Wrong number of values for {operation.__name__} (Expected {values_expected}, got {values_given})")
    
    @property
    def value(self):
        return self.operation(*self.values)
    
    @value.setter
    def value(self, value):
        # Modify the first value using the reverse operation
        try:
            value1 = self.operation.reverse(value, *self.values[1:])
            if value1 is not None:
                self.values[0].__set__(self, value1)
            else:
                raise ValueError(f"Value cannot be set: {self.operation.__name__}({self.values[0]}, <Any>) != {value}")
        except NotImplementedError as e:
            print(e.with_traceback())
            print("Cannot set value for link without reverse operation")