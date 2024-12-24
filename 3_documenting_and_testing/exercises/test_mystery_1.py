import unittest
from mystery_1 import mystery_1


class TestMystery_1(unittest.TestCase):
    """Testing mystery_1"""

    def test_add_numbers(self):
        """Test adding two numbers."""
        self.assertEqual(mystery_1(3, 5), 8)

    def test_add_strings(self):
        """Test adding two strings."""
        self.assertEqual(mystery_1("Hello, ", "world!"), "Hello, world!")

    def test_add_floats(self):
        """Test adding two floats."""
        self.assertEqual(mystery_1(3.5, 2.5), 6.0)  

    def test_add_int_and_float(self):
        """Test adding an int and a float."""
        self.assertEqual(mystery_1(3, 5.5), 8.5)  


