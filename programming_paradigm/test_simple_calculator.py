import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5, "2 + 3 should equal 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "-1 + 1 should equal 0")
        self.assertEqual(self.calc.add(0, 0), 0, "0 + 0 should equal 0")
        self.assertEqual(self.calc.add(-5, -3), -8, "-5 + -3 should equal -8")
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0, "2.5 + 3.5 should equal 6.0")

    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "5 - 3 should equal 2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "-1 - 1 should equal -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "0 - 0 should equal 0")
        self.assertEqual(self.calc.subtract(-5, -3), -2, "-5 - -3 should equal -2")
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0, "5.5 - 2.5 should equal 3.0")

    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "2 * 3 should equal 6")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "-2 * 3 should equal -6")
        self.assertEqual(self.calc.multiply(0, 100), 0, "0 * 100 should equal 0")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "-2 * -3 should equal 6")
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0, "2.5 * 2 should equal 5.0")

    def test_division(self):
        """Test the division method with various inputs and division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2.0, "6 / 3 should equal 2.0")
        self.assertEqual(self.calc.divide(-6, 3), -2.0, "-6 / 3 should equal -2.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "0 / 5 should equal 0.0")
        self.assertEqual(self.calc.divide(-6, -2), 3.0, "-6 / -2 should equal 3.0")
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5, "5.0 / 2.0 should equal 2.5")
        self.assertIsNone(self.calc.divide(10, 0), "10 / 0 should return None")

if __name__ == '__main__':
    unittest.main()
