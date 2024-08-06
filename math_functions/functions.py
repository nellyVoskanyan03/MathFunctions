import math
from .function import Function
from .combined_functions import Operations, SumFunction, SubFunction, MulFunction
from collections import defaultdict
from typing import Union


class Sin(Function):

    def value(self, x) -> float:
        return math.sin(x)

    def derivative(self) -> 'Cos':
        return Cos()

    def _to_string(self, x='x'):
        return f'sin({str(x)})'

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


class Cos(Function):

    def value(self, x) -> float:
        return math.cos(x)

    def derivative(self):
        return Polynomial(0, -1).combine(Sin())

    def _to_string(slef, x='x'):
        return f'cos({str(x)})'

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


class Polynomial(Function):

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.members = args[0]
        else:
            self.members = {i: args[i]
                            for i in range(len(args))}

    def value(self, x) -> float:
        value = 0
        for degree, coefficient in self.members.items():
            value += coefficient * (x ** degree)

        return value

    def derivative(self) -> 'Polynomial':
        result_members = {}
        for degree, coefficient in self.members.items():
            if degree == 0:
                continue
            result_members[degree-1] = degree * coefficient

        return Polynomial(result_members)

    def _to_string(self, x='x'):
        polynomial_str = ''

        for degere, coefficient in self.members.items():
            polynomial_str += f'{coefficient} * {str(x)}^{degere} + '

        return polynomial_str[:len(polynomial_str)-3]

    def __add__(self, other) -> Union['Polynomial', SumFunction]:
        if type(self) is type(other):
            result_members = defaultdict(lambda: 0, self.members)

            for degree, coefficient in other.members.items():
                result_members[degree] += coefficient

            return Polynomial(result_members)
        else:
            return Operations.add(self, other)

    def __sub__(self, other) -> Union['Polynomial', SubFunction]:
        if type(self) is type(other):
            result_members = defaultdict(lambda: 0, self.members)

            for degree, coefficient in other.members.items():
                result_members[degree] -= coefficient

            return Polynomial(result_members)
        else:
            return Operations.sub(self, other)

    def __mul__(self, other) -> Union['Polynomial', MulFunction]:
        if type(self) is type(other):
            result_members = defaultdict(lambda: 0)

            for i, self_coef in self.members.items():
                for j, other_coef in other.members.items():
                    result_members[i + j] += self_coef * other_coef

            return Polynomial(result_members)
        else:
            return Operations.mul(self, other)

    def __truediv__(self, other):
        return Operations.truediv(self, other)

    def combine(self, other):
        return Operations.combine(self, other)
