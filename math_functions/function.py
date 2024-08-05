from abc import ABC, abstractmethod


class Function(ABC):

    def __call__(self, x):
        return self.value(x)

    @abstractmethod
    def value(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def combine(self, other):
        pass
