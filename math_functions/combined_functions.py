from .function import Function


class Operations:

    def add(operand1, operand2):
        return SumFunction(operand1, operand2)

    def sub(operand1, operand2):
        return SubFunction(operand1, operand2)

    def mul(operand1, operand2):
        return MulFunction(operand1, operand2)

    def truediv(operand1, operand2):
        return DivFunction(operand1, operand2)

    def combine(operand1, operand2):
        return CombinedFunction(operand1, operand2)


class CombinedFunction(Function):

    def __init__(self, f, g):
        self.f = f
        self.g = g

    def value(self, x):
        return self.f.value(self.g.value(x))

    def derivative(self):
        return self.f.derivative().combine(self.g) * self.g.derivative()

    def __add__(self, other):
        return Operations.add(self, other)

    def __sub__(self, other):
        return Operations.sub(self, other)

    def __mul__(self, other):
        return Operations.mul(self, other)

    def __truediv__(self, other):
        return Operations.truediv(self, other)

    def combine(self, other):
        return Operations.combine(self, other)


class SumFunction(CombinedFunction):

    def value(self, x):
        return self.f.value(x) + self.g.value(x)

    def derivative(self):
        return self.f.derivative() + self.g.derivative()


class SubFunction(CombinedFunction):

    def value(self, x):
        return self.f.value(x) - self.g.value(x)

    def derivative(self):
        return self.f.derivative() - self.g.derivative()


class MulFunction(CombinedFunction):

    def value(self, x):
        return self.f.value(x) * self.g.value(x)

    def derivative(self):
        return self.f.derivative() * self.g + self.f * self.g.derivative()


class DivFunction(CombinedFunction):

    def value(self, x):
        return self.f.value(x) / self.g.value(x)

    def derivative(self):
        return (self.f.derivative() * self.g - self.f * self.g.derivative()) / (self.g * self.g)
