from math import exp, log


class PEMDAS:
    """
    Enum for the order of operations.
    """
    AS = 0 # Addition, Subtraction
    MD = 1 # Multiplication, Division (and Modulo)
    E = 2 # Exponentiation
    P = 3 # Parentheses


class Operator:
    order = PEMDAS.P
    print_pattern = "$a [operator] $b"
    """
    $a, $b, $c, ... will be replaced by their values based on the _eval method's signature.
    """

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
            cls._eval_reverse(*(2 for _ in range(len(cls._eval_reverse.__code__.co_varnames) - 1)))
            return True
        except NotImplementedError:
            return False        

class EqualOperator(Operator):
    order = PEMDAS.P
    print_pattern = "$a == $b"

    @classmethod
    def _eval(cls, a, b):
        return a == b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return b
        else:
            return None

class NotEqualOperator(Operator):
    order = PEMDAS.P
    print_pattern = "$a != $b"

    @classmethod
    def _eval(cls, a, b):
        return a != b
    
    @classmethod
    def _eval_reverse(cls, b, c):
        if c:
            return None
        else:
            return b

class GreaterOperator(Operator):
    order = PEMDAS.P
    print_pattern = "$a > $b"

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
    order = PEMDAS.P
    print_pattern = "$a >= $b"

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
    order = PEMDAS.P
    print_pattern = "$a < $b"

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
    order = PEMDAS.P
    print_pattern = "$a <= $b"

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
    order = PEMDAS.P
    print_pattern = "$a [number_operator] $b"

    @classmethod
    def _eval(cls, *values):
        return super()._eval(cls)

    @classmethod
    def _eval_reverse(cls, c, b):
        return super()._eval_reverse(c, b)

class AdditionOperator(NumberOperator):
    order = PEMDAS.AS
    print_pattern = "$a + $b"

    @classmethod
    def _eval(cls, a, b):
        return a + b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c - b

class SubtractionOperator(NumberOperator):
    order = PEMDAS.AS
    print_pattern = "$a - $b"

    @classmethod
    def _eval(cls, a, b):
        return a - b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c + b

# All positional operators that have a reverse operation need a
# corresponding backwards operator.
class BackwardsSubtractionOperator(NumberOperator):
    order = PEMDAS.AS
    print_pattern = "$b - $a"

    @classmethod
    def _eval(cls, a, b):
        return b - a
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return b - c

class MultiplicationOperator(NumberOperator):    
    order = PEMDAS.MD
    print_pattern =  "$a * $b"

    @classmethod
    def _eval(cls, a, b):
        return a * b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ZeroDivisionError("tried to divide by zero in MultiplicationOperator.reverse")
        return c / b

class DivisionOperator(NumberOperator):
    order = PEMDAS.MD
    print_pattern = "$a / $b"
 
    @classmethod
    def _eval(cls, a, b):
        if b == 0:
            raise ZeroDivisionError("tried to divide by zero in DivisionOperator")
        return a / b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c * b

class BackwardsDivisionOperator(NumberOperator):
    order = PEMDAS.MD
    print_pattern = "$b / $a"

    @classmethod
    def _eval(cls, a, b):
        if a == 0:
            raise ZeroDivisionError("tried to divide by zero in BackwardsDivide")
        return b / a
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return b / c

class PowerOperator(NumberOperator):
    order = PEMDAS.E
    print_pattern = "$a**$b"

    @classmethod
    def _eval(cls, a, b):
        return a ** b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in PowerOperator.reverse")
        return c ** (1 / b)

class BackwardsPowerOperator(NumberOperator):
    order = PEMDAS.E
    print_pattern = "$b**$a"

    @classmethod
    def _eval(cls, a, b):
        return b ** a
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if c < 0 or b < 0:
            raise ArithmeticError("tried to take logarithm of non positive number in BackwardsPowerOperator.reverse")
        if b == 1:
            raise ArithmeticError("tried divide by zero (log(1)) in BackwardsPowerOperator.reverse")
        return log(c, b)

class RootOperator(NumberOperator):
    order = PEMDAS.E
    print_pattern = "$a**(1/$b)"


    @classmethod
    def _eval(cls, a, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in RootOperator")
        return a ** (1 / b)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in RootOperator.reverse")
        return c ** b


class BackwardsRootOperator(NumberOperator):
    order = PEMDAS.E
    print_pattern = "$b**(1/$a)"

    @classmethod
    def _eval(cls, a, b):
        if a == 0:
            raise ArithmeticError("tried to take zeroth root in BackwardsRootOperator")
        return b ** (1 / a)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b < 0 or c < 0:
            raise ArithmeticError("tried to take logarithm of non positive number in BackwardsRootOperator.reverse")
        if c == 1:
            raise ArithmeticError("tried divide by zero (log(1)) in BackwardsRootOperator.reverse")
        return log(b, c)

class ModuloOperator(NumberOperator):
    order = PEMDAS.MD
    print_pattern = "$a % $b"

    @classmethod
    def _eval(cls, a, b):
        return a % b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        raise NotImplementedError("ModuloOperator does not have a reverse operation")

class AbsoluteOperator(NumberOperator):
    order = PEMDAS.P
    print_pattern = "abs($a)"

    @classmethod
    def _eval(cls, a):
        return abs(a)
    
    @classmethod
    def _eval_reverse(cls, b):
        raise NotImplementedError("AbsOperator does not have a reverse operation")

class NaturalLogarithmOperator(NumberOperator):
    order = PEMDAS.P
    print_pattern = "Ln($a)"

    @classmethod
    def _eval(cls, a):
        return log(a)
    
    @classmethod
    def _eval_reverse(cls, b):
        return exp(b)

class BaseBLogarithmOperator(NumberOperator):
    order = PEMDAS.P
    print_pattern = "LogB($a, $b)"

    @classmethod
    def _eval(cls, a, b):
        return log(a, b)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return b**c
    
class BackwardsBaseBLogarithmOperator(NumberOperator):
    order = PEMDAS.P
    print_pattern = "RLogB($a, $b)"

    @classmethod
    def _eval(cls, a, b):
        return log(b, a)

    @classmethod
    def _eval_reverse(cls, c, b):
        return exp(log(b) / c)


class BooleanOperator(Operator):
    order = PEMDAS.P
    print_pattern = "$a [boolean_operator] $b"

    @classmethod
    def _eval(cls, *values):
        return super()._eval(cls)

    @classmethod
    def _eval_reverse(cls, result, *values):
        return super()._eval_reverse(result, *values)
        
class AndOperator(BooleanOperator): 
    order = PEMDAS.E
    print_pattern = "$a & $b"

    @classmethod
    def _eval(cls, a, b):
        return a & b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == False:
            return None
        else:
            return c
        
class OrOperator(BooleanOperator): 
    order = PEMDAS.MD
    print_pattern = "$a | $b"

    @classmethod
    def _eval(cls, a, b):
        return a | b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == True:
            return None
        else:
            return c

class XorOperator(BooleanOperator):  
    order = PEMDAS.MD
    print_pattern = "$a ^ $b"
  
    @classmethod
    def _eval(cls, a, b):
        return a ^ b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c ^ b

class NotOperator(BooleanOperator):  
    order = PEMDAS.P
    print_pattern = "~$a"
  
    @classmethod
    def _eval(cls, a):
        if isinstance(a, bool):
            return not a
        return ~a
    
    @classmethod
    def _eval_reverse(cls, b):
        if isinstance(b, bool):
            return not b
        return ~b