import unittest
from math_functions import Sin, Cos, Polynomial
import math


class TestFunctions(unittest.TestCase):

    def test_sin_value(self):
        sin = Sin()
        self.assertAlmostEqual(sin.value(math.pi / 2), 1.0)
        self.assertAlmostEqual(sin.value(0), 0.0)

    def test_sin_derivative(self):
        sin = Sin()
        derivative = sin.derivative()
        self.assertAlmostEqual(derivative.value(math.pi / 2), 0.0)
        self.assertAlmostEqual(derivative.value(0), 1.0)

    def test_cos_value(self):
        cos = Cos()
        self.assertAlmostEqual(cos.value(math.pi / 2), 0.0)
        self.assertAlmostEqual(cos.value(0), 1.0)

    def test_derivative(self):
        cos = Cos()
        derivative = cos.derivative()
        self.assertAlmostEqual(derivative.value(math.pi / 2), -1.0)
        self.assertAlmostEqual(derivative.value(0), 0.0)

    def test_polynomial_value(self):
        poly = Polynomial(1, 0, 1)  # 1 + x^2
        self.assertEqual(poly.value(2), 5)
        self.assertEqual(poly.value(0), 1)

    def testt_polynomial_derivative(self):
        poly = Polynomial(1, 0, 1)  # 1 + x^2
        derivative = poly.derivative()
        self.assertEqual(derivative.value(2), 4)
        self.assertEqual(derivative.value(0), 0)


if __name__ == '__main__':
    unittest.main()
