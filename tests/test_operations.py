import unittest
from unittest.mock import MagicMock
from math_functions import Operations, combined_functions


class TestCombinedFunctions(unittest.TestCase):

    def setUp(self):
        self.mock_func1 = MagicMock()
        self.mock_func2 = MagicMock()

        self.mock_func1.value.side_effect = lambda x: x
        self.mock_func2.value.side_effect = lambda x: x

    def test_addition(self):
        add_function = Operations.add(self.mock_func1, self.mock_func2)
        self.assertEqual(add_function(2), 4.0)
        self.assertIsInstance(add_function, combined_functions.SumFunction)

    def test_subtraction(self):
        sub_function = Operations.sub(self.mock_func1, self.mock_func2)
        self.assertEqual(sub_function(2), 0.0)
        self.assertIsInstance(sub_function, combined_functions.SubFunction)

    def test_multiplication(self):
        mul_function = Operations.mul(self.mock_func1, self.mock_func2)
        self.assertEqual(mul_function(2), 4.0)
        self.assertIsInstance(mul_function, combined_functions.MulFunction)

    def test_division(self):
        div_function = Operations.truediv(self.mock_func1, self.mock_func2)
        self.assertEqual(div_function(2), 1.0)
        self.assertIsInstance(div_function, combined_functions.DivFunction)

        self.mock_func2.value.return_value = 0
        with self.assertRaises(ZeroDivisionError):
            Operations.truediv(
                self.mock_func1, self.mock_func2)(0)

    def test_composition(self):
        combined_function = Operations.combine(
            self.mock_func1, self.mock_func2)
        self.assertEqual(combined_function(2), 2.0)
        combined_function = Operations.combine(
            self.mock_func2, self.mock_func1)
        self.assertEqual(combined_function(2), 2.0)
        self.assertIsInstance(
            combined_function, combined_functions.CombinedFunction)


if __name__ == '__main__':
    unittest.main()
