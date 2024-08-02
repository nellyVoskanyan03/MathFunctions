import math
from .function import Function
from .combined_functions import Operations


class Sin(Function):

    def value(self, x):
        return math.sin(x)

    def derivative(self):
        return Cos()

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

    def value(self, x):
        return math.cos(x)

    def derivative(self):
        return Polynomial(0, -1).combine(Sin())

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

    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def value(self, x):
        value = 0
        for i, coefficient in enumerate(self.coefficients):
            value += coefficient * (x ** i)

        return value

    def derivative(self):
        result_coefficients = []
        for i, coefficient in enumerate(self.coefficients):
            result_coefficients.append(i * coefficient)

        return Polynomial(*result_coefficients[1:])

    def __add__(self, other):
        if type(self) is type(other):
            result_coefficients = []

            for self_coef, other_coef in zip(self.coefficients, other.coefficients):
                result_coefficients.append(self_coef + other_coef)

            if len(self.coefficients) != len(other.coefficients):
                min_len = max(len(self.coefficients), len(other.coefficients))

                result_coefficients.extend(self.coefficients[min_len-1:])
                result_coefficients.extend(other.coefficients[min_len-1:])

            return Polynomial(*result_coefficients)
        else:
            return Operations.add(self, other)

    def __sub__(self, other):
        if type(self) is type(other):
            result_coefficients = []

            for self_coef, other_coef in zip(self.coefficients, other.coefficients):
                result_coefficients.append(self_coef - other_coef)

            if len(self.coefficients) != len(other.coefficients):
                min_len = min(len(self.coefficients), len(other.coefficients))

                result_coefficients.extend(self.coefficients[min_len:])
                result_coefficients.extend(other.coefficients[min_len:])

            return Polynomial(*result_coefficients)
        else:
            return Operations.sub(self, other)

    def __mul__(self, other):
        if type(self) is type(other):

            result_len = (len(self.coefficients)) + (len(other.coefficients)-1)
            result_coefficients = [0]*result_len

            for i, self_coef in enumerate(self.coefficients):
                for j, other_coef in enumerate(other.coefficients):
                    result_coefficients[i + j] += self_coef * other_coef

            return Polynomial(*result_coefficients)
        else:
            return Operations.mul(self, other)

    def __truediv__(self, other):
        return Operations.truediv(self, other)

    def combine(self, other):
        return Operations.combine(self, other)
