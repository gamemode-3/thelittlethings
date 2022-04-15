class Operator:
    # TODO: Add proper min and max values
    def __init__(self):
        self.min_values = {}
        self.max_values = {}
    
    def __new__(cls, *args, **kwargs):
        return cls._eval(*args, **kwargs)
    
    @classmethod
    def _eval(cls, *values):
        raise NotImplementedError(f"operation not implemented for {cls.__name__}")

    # Reverse operation.
    # For this:
    # c = Operation().call(a, b)
    # This should be true:
    # a = Operation().reverse(b, c)  
    @classmethod
    def _eval_reverse(cls, result, *values):
        raise NotImplementedError(f"reverse operation not implemented for {cls.__name__}")

    @classmethod
    def reverse(cls, result, *values):
        return cls._eval_reverse(result, *values)

    @classmethod
    def has_reverse(cls):
        try:
            cls._eval_reverse(*(1 for _ in range(len(cls._eval_reverse.__code__.co_varnames) - 1)))
            return True
        except NotImplementedError:
            return False        

class ValueOperator(Operator):
    @classmethod
    def _eval(cls, a):
        return a
    
    @classmethod
    def _eval_reverse(cls, b):
        return b

class EqualOperator(Operator):
    @classmethod
    def _eval(cls, a, b):
        return a == b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return b
        else:
            return None

class GreaterOperator(Operator):
    @classmethod
    def _eval(cls, a, b):
        return a > b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return b
        else:
            return None

class GreaterEqualOperator(Operator):
    @classmethod
    def _eval(cls, a, b):
        return a >= b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return b
        else:
            return None

class LessOperator(Operator):
    @classmethod
    def _eval(cls, a, b):
        return a < b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return b
        else:
            return None
            
class LessEqualOperator(Operator):
    @classmethod
    def _eval(cls, a, b):
        return a <= b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return b
        else:
            return None


class NumberOperator(Operator):
    @classmethod
    def _eval(cls, *values):
        return super()._eval(cls)

    @classmethod
    def _eval_reverse(cls, c, b):
        return super()._eval_reverse(c, b)

class AdditionOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a + b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c - b

class SubtractionOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a - b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c + b

# All positional operators that have a reverse operation need a
# corresponding backwards operator.
class BackwardsSubtractionOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return b - a
    
    @classmethod
    def _eval_reverse(cls, c, a):
        return c + a

class MultiplicationOperator(NumberOperator):     
    @classmethod
    def _eval(cls, a, b):
        return a * b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ZeroDivisionError("tried to divide by zero in MultiplicationOperator.reverse")
        return c / b

class DivisionOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        if b == 0:
            raise ZeroDivisionError("tried to divide by zero in DivisionOperator")
        return a / b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c * b

class BackwardsDivisionOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        if a == 0:
            raise ZeroDivisionError("tried to divide by zero in BackwardsDivide")
        return b / a
    
    @classmethod
    def _eval_reverse(cls, c, a):
        return c * a

class PowerOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a ** b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in PowerOperator.reverse")
        return c ** (1 / b)

class BackwardsPowerOperator(NumberOperator):
    @classmethod
    def _eval(cls, a, b):
        return b ** a
    
    @classmethod
    def _eval_reverse(cls, c, a):
        if a == 0:
            raise ArithmeticError("tried to take zeroth root in BackwardsPowerOperator.reverse")
        return c ** (1 / a)

class RootOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in RootOperator")
        return a ** (1 / b)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c ** b

class BackwardsRootOperator(NumberOperator):
    @classmethod
    def _eval(cls, a, b):
        if a == 0:
            raise ArithmeticError("tried to take zeroth root in BackwardsRootOperator")
        return b ** (1 / a)
    
    @classmethod
    def _eval_reverse(cls, c, a):
        return c ** a

class ModuloOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a % b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        raise NotImplementedError("ModuloOperator does not have a reverse operation")

class AbsoluteOperator(NumberOperator):    
    @classmethod
    def _eval(cls, a):
        return abs(a)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        raise NotImplementedError("AbsOperator does not have a reverse operation")

class BooleanOperator(Operator):
    @classmethod
    def _eval(cls, *values):
        return super()._eval(cls)

    @classmethod
    def _eval_reverse(cls, result, *values):
        return super()._eval_reverse(result, *values)
        
class AndOperator(BooleanOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a and b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == False:
            return None
        else:
            return c

class OrOperator(BooleanOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a or b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == True:
            return None
        else:
            return c

class XorOperator(BooleanOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a ^ b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c ^ b

class NotOperator(BooleanOperator):    
    @classmethod
    def _eval(cls, a):
        return not a
    
    @classmethod
    def _eval_reverse(cls, b):
        return not b