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

class mpNumberFormat(enum.Enum):
    DECIMAL = 0
    OCTAL = 1
    HEXADECIMAL = 2
    BINARY = 3

class mpElement:
    def __init__(self):
        self.evaluable = True

    def evaluate(self):
        pass

    def negate(self):
        pass

    def format(self):
        pass

class mpNumber(mpElement):
    def __init__(self, value: float, format: mpNumberFormat):
        self.val = 0
        self.mp_format = format

    def evaluate(self):
        self.evaluable = True
        if self.val == 0:
            return None
        return self
    
    def negate(self):
        self.val *= -1
        return self.val
    
    def format(self):
        return str(self.val)
    
    def value(self, mp_format: mpNumberFormat):
        if mp_format == mpNumberFormat.DECIMAL:
            return str(self.val)
        if mp_format == mpNumberFormat.HEXADECIMAL:
            return hex(self.val)
        if mp_format == mpNumberFormat.BINARY:
            return bin(self.val)
        if mp_format == mpNumberFormat.OCTAL:
            return oct(self.val)

class mpBinary(mpElement):
    def __init__(self, lhs: mpElement, rhs: mpElement, op: mpOperator):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        self.evaluable = self.lhs.evaluable and self.rhs.evaluable

    def evaluate(self):
        self.lhs = self.lhs.evaluate()
        self.rhs = self.rhs.evaluate()

        if self.lhs is None:
            if self.op == mpOperator.ADDITION:
                return self.rhs
            if self.op == mpOperator.SUBTRACTION:
                return mpUnary(self.rhs, mpUnaryOperator.MINUS)
            if self.op == mpOperator.MULTIPLICATION or self.op == mpOperator.DIVISION:
                return mpNumber(0, mpNumberFormat.DECIMAL)
        if self.rhs is None:
            if self.op == mpOperator.ADDITION:
                return self.lhs
            if self.op == mpOperator.SUBTRACTION:
                return mpUnary(self.lhs, mpUnaryOperator.MINUS)
            if self.op == mpOperator.MULTIPLICATION or self.op == mpOperator.DIVISION:
                return mpNumber(0, mpNumberFormat.DECIMAL)
    
    def negate(self):
        return 
    
    def format(self):
        if isinstance(self.rhs, mpUnary):
            if self.op == mpOperator.ADDITION:
                return "(" + self.lhs.format() + "+" + self.rhs.format() + ")"
            if self.op == mpOperator.SUBTRACTION:
                return "(" + self.lhs.format() + "-" + self.rhs.format() + ")"
        if isinstance(self.rhs, mpNumber):
            if self.op == mpOperator.ADDITION and self.rhs.value() < 0:
                return "(" + self.lhs.format() + "-" + self.rhs.format() + ")"
        return "(" + self.lhs.format() + self.op2str(self.op) + self.rhs.format() + ")"
    
    def applyOperator(self, lhs: mpNumber, rhs: mpNumber, op: mpOperator):
        if op == mpOperator.ADDITION:
            return mpNumber(lhs.value() + rhs.value(), mpNumberFormat.DECIMAL)
        if op == mpOperator.SUBTRACTION:
            return mpNumber(lhs.value() - rhs.value(), mpNumberFormat.DECIMAL)
        if op == mpOperator.MULTIPLICATION:
            return mpNumber(lhs.value() * rhs.value(), mpNumberFormat.DECIMAL)
        if op == mpOperator.DIVISION:
            return mpNumber(lhs.value() / rhs.value(), mpNumberFormat.DECIMAL)
        if op == mpOperator.EXPONENT:
            return mpNumber(pow(lhs.value(), rhs.value()), mpNumberFormat.DECIMAL)
        if op == mpOperator.MODULO:
            return mpNumber(lhs.value() % rhs.value(), mpNumberFormat.DECIMAL)
        raise NotImplementedError("This operator is not implemented.")
    
    def op2str(self, op: mpOperator):
        if op == mpOperator.NOP:
            return ""
        if op == mpOperator.ADDITION:
            return "+"
        if op == mpOperator.SUBTRACTION:
            return "-"
        if op == mpOperator.MULTIPLICATION:
            return "*"
        if op == mpOperator.DIVISION:
            return "/"
        if op == mpOperator.EXPONENT:
            return "^"
        if op == mpOperator.MODULO:
            return "%"
        raise NotImplementedError("This operator is not implemented.")

class mpPriority(mpElement):
    def __init__(self, element: mpElement):
        self.element = element

    def evaluate(self):
        return self.element.evaluate()
    
    def negate(self):
        return mpUnary(self.element, mpUnaryOperator.MINUS)
    
    def format(self):
        return "(" + self.element.format() + ")"

class mpUnary(mpElement):
    def __init__(self, element: mpElement, op: mpUnaryOperator):
        self.element = element
        self.op = op
        self.evaluable = element.evaluable

    def evaluate(self):
        self.element = self.element.evaluate()
        if self.op == mpUnaryOperator.MINUS and self.element is not None:
            self.element = self.element.negate()
        return self.element
    
    def negate(self):
        if self.op == mpUnaryOperator.MINUS:
            return self.element
        else:
            return mpUnary(self.element, mpUnaryOperator.MINUS)

    def format(self):
        if self.op == mpUnaryOperator.MINUS and self.element is not None:
            return "-" + self.element.format()
        return "null"

class mpVariable(mpElement):
    def __init__(self, name: str):
        self.var_name = name

    def evaluate(self):
        return self
    
    def negate(self):
        return mpUnary(self, mpUnaryOperator.MINUS)
    
    def format(self):
        return self.var_name

class Parser:
    def __init__(self):
        self.original_expression = None
        self.char_idx = 0

    def parse(self, expression):
        self.original_expression = expression
        self.expression = ""
        
        self.expression = self.expression.trim() + ("" if self.expression.endsWith(";") else ";")

        self.char_idx = 0
