import unittest
from math_functions import Polynomial


class TestCombinedFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create mock functions for f and g
        cls.f = Polynomial(0, 1)
        cls.g = Polynomial(1, 1)

    def test_div_function_derivative(self):

        derivative = (self.f / self.g).derivative()
        # Expected derivative: (f'(x) * g(x) - f(x) * g'(x)) / (g(x) * g(x))
        # f'(x) = 1, g'(x) = 1
        # f(x) = x, g(x) = x + 1
        # Expected: (1 * (x + 1) - x * 1) / (x + 1)^2
        #          = 1 / (x + 1)^2

        # Configure the mocks for specific values

        # Test at specific points
        x = 2
        expected_value = 1/(x ** 2 + 2*x + 1)
        self.assertEqual(derivative.value(x), expected_value)

    def test_sum_function_derivative(self):

        derivative = (self.f + self.g).derivative()
        # Expected derivative: (f'(x) + g'(x))
        # f'(x) = 1, g'(x) = 1
        # Expected: 2

        # Test at specific points
        x = 2
        expected_value = 2
        self.assertEqual(derivative.value(x), expected_value)

    def test_sub_function_derivative(self):

        derivative = (self.f - self.g).derivative()
        # Expected derivative: (f'(x) - g'(x))
        # f'(x) = 1, g'(x) = 1
        # Expected: 0

        # Test at specific points
        x = 2
        expected_value = 0
        self.assertEqual(derivative.value(x), expected_value)

    def test_mul_function_derivative(self):

        derivative = (self.f * self.g).derivative()
        # Expected derivative: (f'(x) * g(x) + f(x) * g'(x))
        # f'(x) = 1, g'(x) = 1
        # Expected: g(x) + f(x)

        # Test at specific points
        x = 2
        expected_value = 5
        self.assertEqual(derivative.value(x), expected_value)


if __name__ == '__main__':
    unittest.main()
