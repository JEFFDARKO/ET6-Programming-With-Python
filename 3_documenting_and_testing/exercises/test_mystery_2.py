import unittest
from mystery_2 import mystery_2 

class TestMystery_2(unittest.TestCase):
    """Test cases for the mystery_2 function"""

    def test_empty_list(self):
        self.assertIsNone(mystery_2([]))

    def test_empty_string(self):
        self.assertIsNone(mystery_2(""))

    def test_non_empty_list(self):
        self.assertEqual(mystery_2([1, 2, 3]), 3)

    def test_non_empty_string(self):
        self.assertEqual(mystery_2("Jeffery"), 7)

    def test_single_element_list(self):
        self.assertEqual(mystery_2([10]), 1)

    def test_single_character_string(self):
        self.assertEqual(mystery_2("A"), 1)

    def test_tuple(self):
        self.assertEqual(mystery_2((1, 2, 3, 4)), 4)

    def test_empty_tuple(self):
        self.assertIsNone(mystery_2(()))

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            mystery_2(5)

    def test_mixed_elements_list(self):
        self.assertEqual(mystery_2([1, "hello", 3.5]), 3)

