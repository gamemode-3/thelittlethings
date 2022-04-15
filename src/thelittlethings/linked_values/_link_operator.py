class Operator:
    # TODO: Add proper min and max values
    def __init__(self):
        self.min_values = {}
        self.max_values = {}
    
    def __new__(cls, *args, **kwargs):
        cls._eval(*args, **kwargs)
    
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

class NumberOperator(Operator):
    @classmethod
    def _eval(cls, *values):
        return super()._eval(cls)

    @classmethod
    def _eval_reverse(cls, c, b):
        return super()._eval_reverse(c, b)

class Add(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a + b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c - b

class Substract(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a - b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c + b

class Multiply(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a * b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ZeroDivisionError("tried to divide by zero in Multiply.reverse")
        return c / b

class Divide(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        if b == 0:
            raise ZeroDivisionError("tried to divide by zero in Divide")
        return a / b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c * b

class Power(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a ** b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in Power.reverse")
        return c ** (1 / b)

class Root(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        if b == 0:
            raise ArithmeticError("tried to take zeroth root in Root")
        return a ** (1 / b)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        return c ** b

class Modulo(NumberOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a % b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        raise NotImplementedError("Modulo does not have a reverse operation")

class Absolute(NumberOperator):    
    @classmethod
    def _eval(cls, a):
        return abs(a)
    
    @classmethod
    def _eval_reverse(cls, c, b):
        raise NotImplementedError("Abs does not have a reverse operation")

class BooleanOperator(Operator):
    @classmethod
    def _eval(cls, *values):
        return super()._eval(cls)

    @classmethod
    def _eval_reverse(cls, result, *values):
        return super()._eval_reverse(result, *values)
        
class And(BooleanOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a and b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == False:
            return None
        else:
            return c

class Or(BooleanOperator):    
    @classmethod
    def _eval(cls, a, b):
        return a or b
    
    @classmethod
    def _eval_reverse(cls, c, b):
        if b == True:
            return None
        else:
            return c

class Not(BooleanOperator):    
    @classmethod
    def _eval(cls, a):
        return not a
    
    @classmethod
    def _eval_reverse(cls, b):
        return not b
