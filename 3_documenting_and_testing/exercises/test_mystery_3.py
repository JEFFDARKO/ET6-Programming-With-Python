import unittest


from mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    def test_smaller_number_eg1(self):
        self.assertEqual(mystery_3(2, 5), 2)
        
    def test_smaller_number_eg2(self):
        self.assertEqual(mystery_3(10, 3), 3)
        
    def test_smaller_number_eg3(self):
        self.assertEqual(mystery_3(-1, 1), -1)

    def test_equal_numbers_eg1(self):
        self.assertEqual(mystery_3(7, 7), 14)
        
    def test_equal_numbers_eg2(self):
        self.assertEqual(mystery_3(0, 0), 0)
        
    def test_equal_numbers_eg3(self):
        self.assertEqual(mystery_3(-3, -3), -6)

    def test_floats_eg1(self):
        self.assertEqual(mystery_3(3.5, 7.2), 3.5)
        
    def test_floats_eg2(self):
        self.assertEqual(mystery_3(5.5, 5.5), 11.0)

    def test_mixed_int_float_eg1(self):
        self.assertEqual(mystery_3(3, 3.0), 6.0)
        
    def test_mixed_int_float_eg2(self):
        self.assertEqual(mystery_3(4.5, 2), 2.0)