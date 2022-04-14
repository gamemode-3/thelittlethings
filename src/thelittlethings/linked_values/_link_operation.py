class Operation:
    # TODO: Add proper min and max values
    def __init__(self):
        self.min_values = {}
        self.max_values = {}
    
    def __new__(cls, *values):
        raise NotImplementedError(f"Operation not implemented for {cls.__name__}")

    # Reverse operation.
    # For this:
    # c = Operation().call(a, b)
    # This should be true:
    # a = Operation().reverse(b, c)    
    @classmethod
    def reverse(cls, result, *values):
        raise NotImplementedError(f"Reverse operation not implemented for {cls.__name__}")

    @classmethod
    def has_reverse(cls):
        try:
            cls.reverse(*(1 for _ in range(len(cls.reverse.__code__.co_varnames) - 1)))
            return True
        except NotImplementedError:
            return False        

class NumberOperation(Operation):
    def __new__(cls, *values):
        return super().__new__(cls)

    @classmethod
    def reverse(cls, c, b):
        return super().reverse(c, b)

class Add(NumberOperation):    
    def __new__(cls, a, b):
        return a + b
    
    @classmethod
    def reverse(cls, c, b):
        return c - b

class Substract(NumberOperation):    
    def __new__(cls, a, b):
        return a - b
    
    @classmethod
    def reverse(cls, c, b):
        return c + b

class Multiply(NumberOperation):    
    def __new__(cls, a, b):
        return a * b
    
    @classmethod
    def reverse(cls, c, b):
        if b == 0:
            raise ZeroDivisionError("Tried to divide by zero in Multiply.reverse")
        return c / b

class Divide(NumberOperation):    
    def __new__(cls, a, b):
        if b == 0:
            raise ZeroDivisionError("Tried to divide by zero in Divide")
        return a / b
    
    @classmethod
    def reverse(cls, c, b):
        return c * b

class Power(NumberOperation):    
    def __new__(cls, a, b):
        return a ** b
    
    @classmethod
    def reverse(cls, c, b):
        if b == 0:
            raise ArithmeticError("Tried to take zeroth root in Power.reverse")
        return c ** (1 / b)

class Root(NumberOperation):    
    def __new__(cls, a, b):
        if b == 0:
            raise ArithmeticError("Tried to take zeroth root in Root")
        return a ** (1 / b)
    
    @classmethod
    def reverse(cls, c, b):
        return c ** b

class Modulo(NumberOperation):    
    def __new__(cls, a, b):
        return a % b
    
    @classmethod
    def reverse(cls, c, b):
        raise NotImplementedError("Modulo does not have a reverse operation")

class Abs(NumberOperation):    
    def __new__(cls, a):
        return abs(a)
    
    @classmethod
    def reverse(cls, c, b):
        raise NotImplementedError("Abs does not have a reverse operation")

class BooleanOperation(Operation):
    def __new__(cls, *values):
        return super().__new__(cls)

    @classmethod
    def reverse(cls, result, *values):
        return super().reverse(result, *values)
        
class And(BooleanOperation):    
    def __new__(cls, a, b):
        return a and b
    
    @classmethod
    def reverse(cls, c, b):
        if b == False:
            return None
        else:
            return c

class Or(BooleanOperation):    
    def __new__(cls, a, b):
        return a or b
    
    @classmethod
    def reverse(cls, c, b):
        if b == True:
            return None
        else:
            return c

class Not(BooleanOperation):    
    def __new__(cls, a):
        return not a
    
    @classmethod
    def reverse(cls, b):
        return not b

