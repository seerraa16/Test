import unittest
import math
from src import calculator, add, subtract, multiply, divide, power, sqrt, sin, cos, tan, factorial
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 0), "Error! Division by zero.")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -2), 0.25)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(0), 0)

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(180), 0)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(180), -1)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(90), math.inf)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

if __name__ == '__main__':
    unittest.main()