from .function import Function


class Operations:
    @staticmethod
    def add(operand1: 'Function', operand2: 'Function') -> 'SumFunction':
        return SumFunction(operand1, operand2)

    @staticmethod
    def sub(operand1: 'Function', operand2: 'Function') -> 'SubFunction':
        return SubFunction(operand1, operand2)

    @staticmethod
    def mul(operand1: 'Function', operand2: 'Function') -> 'MulFunction':
        return MulFunction(operand1, operand2)

    @staticmethod
    def truediv(operand1: 'Function', operand2: 'Function') -> 'DivFunction':
        return DivFunction(operand1, operand2)

    @staticmethod
    def combine(operand1: 'Function', operand2: 'Function') -> 'CombinedFunction':
        return CombinedFunction(operand1, operand2)


class CombinedFunction(Function):

    def __init__(self, f: 'Function', g: 'Function'):
        self.f = f
        self.g = g

    def value(self, x):
        return self.f.value(self.g.value(x))

    def derivative(self) -> 'CombinedFunction':
        return self.f.derivative().combine(self.g) * self.g.derivative()

    def _to_string(self) -> str:
        return self.f._to_string(self.g)

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
    def _to_string(self):
        return f'({str(self.f)}) + ({str(self.g)})'

    def value(self, x):
        return self.f.value(x) + self.g.value(x)

    def derivative(self) -> 'SumFunction':
        return self.f.derivative() + self.g.derivative()


class SubFunction(CombinedFunction):
    def _to_string(self):
        return f'({str(self.f)}) - ({str(self.g)})'

    def value(self, x):
        return self.f.value(x) - self.g.value(x)

    def derivative(self) -> 'SubFunction':
        return self.f.derivative() - self.g.derivative()


class MulFunction(CombinedFunction):
    def _to_string(self):
        return f'({str(self.f)}) * ({str(self.g)})'

    def value(self, x):
        return self.f.value(x) * self.g.value(x)

    def derivative(self) -> 'SumFunction':
        return self.f.derivative() * self.g + self.f * self.g.derivative()


class DivFunction(CombinedFunction):
    def _to_string(self):
        return f'({str(self.f)}) / ({str(self.g)})'

    def value(self, x):
        if self.g.value(x) == 0:
            raise ZeroDivisionError(
                f'Value of divisor function for x = {x} is 0')
        else:
            return self.f.value(x) / self.g.value(x)

    def derivative(self) -> 'DivFunction':
        return (self.f.derivative() * self.g - self.f * self.g.derivative()) / (self.g * self.g)
