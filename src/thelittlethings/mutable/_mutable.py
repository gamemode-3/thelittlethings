from typing import Generic, TypeVar

T = TypeVar('T')

class Mutable(Generic[T]):
    '''
    mutable value to be passed by reference.
    implements dunder methods to point to the value.
    '''
    def __init__(self, value: T):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        self.value = value
    
    def __delete__(self, instance):
        self.value = None
    
    def __call__(self, *args, **kwargs):
        return self.value()
    
    def __len__(self):
        return self.value.__len__()
    
    def __getitem__(self, key):
        return self.value.__getitem__(key)
    
    def __setitem__(self, key, value):
        self.value.__setitem__(key, value)
    
    def __delitem__(self, key):
        self.value.__delitem__(key)
    
    def __iter__(self):
        return self.value.__iter__()
    
    def __contains__(self, item):
        return self.value.__contains__(item)
    
    def __add__(self, other):
        if isinstance(other, Mutable):
            return self.value.__add__(other.value)
        else:
            return self.value.__add__(other)
        
    def __radd__(self, other):
        if isinstance(other, Mutable):
            return self.value.__radd__(other.value)
        else:
            return self.value.__radd__(other)
    
    def __iadd__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__iadd__(other.value)
            else:
                return self.value.__iadd__(other)
        except AttributeError:
            self.value = self.value.__add__(other)
            return self.value
    
    def __sub__(self, other):
        if isinstance(other, Mutable):
            return self.value.__sub__(other.value)
        else:
            return self.value.__sub__(other)
    
    def __rsub__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rsub__(other.value)
        else:
            return self.value.__rsub__(other)
    
    def __isub__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__isub__(other.value)
            else:
                return self.value.__isub__(other)
        except AttributeError:
            self.value = self.value.__sub__(other)
            return self.value

    def __mul__(self, other):
        if isinstance(other, Mutable):
            return self.value.__mul__(other.value)
        else:
            return self.value.__mul__(other)
    
    def __rmul__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rmul__(other.value)
        else:
            return self.value.__rmul__(other)
    
    def __imul__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__imul__(other.value)
            else:
                return self.value.__imul__(other)
        except AttributeError:
            self.value = self.value.__mul__(other)
            return self.value

    def __truediv__(self, other):
        if isinstance(other, Mutable):
            return self.value.__truediv__(other.value)
        else:
            return self.value.__truediv__(other)
    
    def __rtruediv__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rtruediv__(other.value)
        else:
            return self.value.__rtruediv__(other)
    
    def __itruediv__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__itruediv__(other.value)
            else:
                return self.value.__itruediv__(other)
        except AttributeError:
            self.value = self.value.__truediv__(other)
            return self.value

    def __floordiv__(self, other):
        if isinstance(other, Mutable):
            return self.value.__floordiv__(other.value)
        else:
            return self.value.__floordiv__(other)
    
    def __rfloordiv__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rfloordiv__(other.value)
        else:
            return self.value.__rfloordiv__(other)
    
    def __ifloordiv__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__ifloordiv__(other.value)
            else:
                return self.value.__ifloordiv__(other)
        except AttributeError:
            self.value = self.value.__floordiv__(other)
            return self.value

    def __mod__(self, other):
        if isinstance(other, Mutable):
            return self.value.__mod__(other.value)
        else:
            return self.value.__mod__(other)
    
    def __rmod__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rmod__(other.value)
        else:
            return self.value.__rmod__(other)
    
    def __imod__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__imod__(other.value)
            else:
                return self.value.__imod__(other)
        except AttributeError:
            self.value = self.value.__mod__(other)
            return self.value

    def __pow__(self, other):
        if isinstance(other, Mutable):
            return self.value.__pow__(other.value)
        else:
            return self.value.__pow__(other)
    
    def __rpow__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rpow__(other.value)
        else:
            return self.value.__rpow__(other)
    
    def __ipow__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__ipow__(other.value)
            else:
                return self.value.__ipow__(other)
        except AttributeError:
            self.value = self.value.__pow__(other)
            return self.value

    def __lt__(self, other):
        if isinstance(other, Mutable):
            return self.value.__lt__(other.value)
        else:
            return self.value.__lt__(other)
    
    def __le__(self, other):
        if isinstance(other, Mutable):
            return self.value.__le__(other.value)
        else:
            return self.value.__le__(other)
    
    def __eq__(self, other):
        if isinstance(other, Mutable):
            return self.value.__eq__(other.value)
        else:
            return self.value.__eq__(other)
    
    def __ne__(self, other):
        if isinstance(other, Mutable):
            return self.value.__ne__(other.value)
        else:
            return self.value.__ne__(other)
    
    def __ge__(self, other):
        if isinstance(other, Mutable):
            return self.value.__ge__(other.value)
        else:
            return self.value.__ge__(other)
    
    def __gt__(self, other):
        if isinstance(other, Mutable):
            return self.value.__gt__(other.value)
        else:
            return self.value.__gt__(other)
    
    def __and__(self, other):
        if isinstance(other, Mutable):
            return self.value.__and__(other.value)
        else:
            return self.value.__and__(other)
    
    def __rand__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rand__(other.value)
        else:
            return self.value.__rand__(other)
    
    def __iand__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__iand__(other.value)
            else:
                return self.value.__iand__(other)
        except AttributeError:
            self.value = self.value.__and__(other)
            return self.value

    def __or__(self, other):
        if isinstance(other, Mutable):
            return self.value.__or__(other.value)
        else:
            return self.value.__or__(other)
    
    def __ror__(self, other):
        if isinstance(other, Mutable):
            return self.value.__ror__(other.value)
        else:
            return self.value.__ror__(other)
    
    def __ior__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__ior__(other.value)
            else:
                return self.value.__ior__(other)
        except AttributeError:
            self.value = self.value.__or__(other)
            return self.value

    def __xor__(self, other):
        if isinstance(other, Mutable):
            return self.value.__xor__(other.value)
        else:
            return self.value.__xor__(other)
    
    def __rxor__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rxor__(other.value)
        else:
            return self.value.__rxor__(other)
    
    def __ixor__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__ixor__(other.value)
            else:
                return self.value.__ixor__(other)
        except AttributeError:
            self.value = self.value.__xor__(other)
            return self.value

    def __lshift__(self, other):
        if isinstance(other, Mutable):
            return self.value.__lshift__(other.value)
        else:
            return self.value.__lshift__(other)
    
    def __rlshift__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rlshift__(other.value)
        else:
            return self.value.__rlshift__(other)
    
    def __ilshift__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__ilshift__(other.value)
            else:
                return self.value.__ilshift__(other)
        except AttributeError:
            self.value = self.value.__lshift__(other)
            return self.value    

    def __rshift__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rshift__(other.value)
        else:
            return self.value.__rshift__(other)
    
    def __rrshift__(self, other):
        if isinstance(other, Mutable):
            return self.value.__rrshift__(other.value)
        else:
            return self.value.__rrshift__(other)
    
    def __irshift__(self, other):
        try:
            if isinstance(other, Mutable):
                return self.value.__irshift__(other.value)
            else:
                return self.value.__irshift__(other)
        except AttributeError:
            self.value = self.value.__rshift__(other)
            return self.value

    def __neg__(self):
        return self.value.__neg__()
    
    def __pos__(self):
        return self.value.__pos__()
    
    def __abs__(self):
        return self.value.__abs__()
    
    def __invert__(self):
        return self.value.__invert__()
    
    def __complex__(self):
        return self.value.__complex__()
    
    def __int__(self):
        return self.value.__int__()
    
    def __float__(self):
        return self.value.__float__()

    def __round__(self, n=0):
        return self.value.__round__(n)
    
    def __index__(self):
        return self.value.__index__()
    
    def __coerce__(self, other):
        return self.value.__coerce__(other)
    
    def __oct__(self):
        return self.value.__oct__()
    
    def __hex__(self):
        return self.value.__hex__()
    
    def __trunc__(self):
        return self.value.__trunc__()
    
    def __floor__(self):
        return self.value.__floor__()
    
    def __ceil__(self):
        return self.value.__ceil__()
    
    def __bool__(self):
        return self.value.__bool__()