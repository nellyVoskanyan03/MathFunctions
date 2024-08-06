from abc import ABC, abstractmethod


class Function(ABC):

    def __call__(self, x):
        return self.value(x)

    def __str__(self):
        return self._to_string()

    @abstractmethod
    def value(self, x):
        pass

    @abstractmethod
    def derivative(self) -> 'Function':
        pass

    @abstractmethod
    def _to_string(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: 'Function') -> 'Function':
        pass

    @abstractmethod
    def __sub__(self, other: 'Function') -> 'Function':
        pass

    @abstractmethod
    def __mul__(self, other: 'Function') -> 'Function':
        pass

    @abstractmethod
    def __truediv__(self, other: 'Function') -> 'Function':
        pass

    @abstractmethod
    def combine(self, other: 'Function') -> 'Function':
        pass
