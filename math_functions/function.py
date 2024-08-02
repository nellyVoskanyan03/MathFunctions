class Function:

    def __call__(self, x):
        return self.value(x)

    def value(self, x):
        raise NotImplementedError('Function is not fully implemented')

    def derivative(self):
        raise NotImplementedError('Function is not fully implemented')

    def __add__(self, other):
        raise NotImplementedError('Function is not fully implemented')

    def __sub__(self, other):
        raise NotImplementedError('Function is not fully implemented')

    def __mul__(self, other):
        raise NotImplementedError('Function is not fully implemented')

    def __truediv__(self, other):
        raise NotImplementedError('Function is not fully implemented')

    def apply(self, other):
        raise NotImplementedError('Function is not fully implemented')
