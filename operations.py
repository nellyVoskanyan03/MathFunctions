class Function:

    def __call__(self, x):
        return self.value(x)
    
    def value(self, x):
        raise NotImplementedError('Function is not fully implemented')
    
    def derivative(self):
        raise NotImplementedError('Function is not fully implemented')
   
    def __add__(self, other):
        return Operations.add(self, other)

    def __sub__(self, other):
        return Operations.sub(self, other)

    def __mul__(self, other):
        return Operations.mul(self, other)

    def __truediv__(self, other):
        return Operations.truediv(self, other)

    def apply(self, other):
        return Operations.apply(self, other)


class Operations:

    def add(operand1, operand2):
        return SumFunction(operand1, operand2)

    def sub(operand1, operand2):
        return SubFunction(operand1, operand2)

    def mul(operand1, operand2):
        return MulFunction(operand1, operand2)

    def truediv(operand1, operand2):
        return DivFunction(operand1, operand2)

    def apply(operand1, operand2):
        return AppliedFunction(operand1, operand2)  


class SumFunction(Function):

    def __init__(self, augent, addend):
        self.augent = augent
        self.addend = addend

    def value(self, x):
        return self.augent.value(x) + self.addend.value(x)
    
    def derivative(self):
        return self.augent.derivative() + self.addend.derivative()


class SubFunction(Function):
    def __init__(self, minuend, subtraend):
        self.minuend = minuend
        self.subtraend = subtraend

    def value(self, x):
        return self.minuend.value(x) - self.subtraend.value(x)
    
    def derivative(self):
        return self.minuend.derivative() - self.subtraend.derivative()


class MulFunction(Function):
    def __init__(self, multiplier, multiplicand):
        self.multiplier = multiplier
        self.multiplicand = multiplicand

    def value(self, x):
        return self.multiplier.value(x) * self.multiplicand.value(x)
    
    def derivative(self):
        return self.multiplier.derivative() * self.multiplicand + self.multiplier * self.multiplicand.derivative()


class DivFunction(Function):
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def value(self, x):
        return self.dividend.value(x) / self.divisor.value(x)
    
    def derivative(self):
        return (self.dividend.derivative() * self.divisor - self.dividend * self.divisor.derivative()) / (self.divisor * self.divisor)



class AppliedFunction(Function):
    def __init__(self, base_function, inner_function):
        self.base_function = base_function
        self.inner_function = inner_function

    def value(self, x):
        return self.base_function.value(self.inner_function.value(x))
    
    def derivative(self):
        return self.base_function.derivative().apply(self.inner_function) * self.inner_function.derivative()

