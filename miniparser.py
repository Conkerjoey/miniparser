import os
import enum


class mpUnaryOperator(enum.Enum):
    NOP = 0
    MINUS = 1

class mpOperator(enum.Enum):
    NOP = 0
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4
    EXPONENT =  5
    MODULO = 6

class mpElement:
    def __init__(self):
        self.evaluable = True

    def evaluate(self):
        pass

    def negate(self):
        pass

class mpBinary(mpElement):
    def __init__(self):
        pass

class mpNumber(mpElement):
    def __init__(self):
        pass

class mpPriority(mpElement):
    def __init__(self):
        pass

class mpUnary(mpElement):
    def __init__(self, element: mpElement, op: mpUnaryOperator):
        self.element = element
        self.op = op
        self.evaluable = element.evaluable

    def evaluate(self)
        self.element = self.element.evaluate()
        if self.element is not None:
            self.element = self.element.negate()

class mpVariable(mpElement):
    def __init__(self, name: str):
        self.var_name = name

    def evaluate(self):
        return self
    
    def negate(self):
        return mpUnary(self, mpUnaryOperator.MINUS)

class Parser:
    def __init__(self):
        self.original_expression = None
        self.char_idx = 0

    def parse(self, expression):
        self.original_expression = expression
        self.expression = ""
        
        self.expression = self.expression.trim() + ("" if self.expression.endsWith(";") else ";")

        self.char_idx = 0
