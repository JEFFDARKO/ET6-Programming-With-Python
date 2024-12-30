import unittest
from ..sum_evens_and_odds import sum_evens_and_odds

class TestSumEvensAndOdds(unittest.TestCase):
    """Tests for the sum_evens_and_odds function"""

    def test_should_return_sum_of_even_and_odd_numbers(self):
        """Test case where the sum of even and odd numbers is returned."""
        self.assertEqual(sum_evens_and_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), {'evens': 30, 'odds': 25})

    def test_should_handle_empty_list(self):
        """Test case with an empty list."""
        self.assertEqual(sum_evens_and_odds([]), {'evens': 0, 'odds': 0})

    def test_should_handle_all_odd_numbers(self):
        """Test case with only odd numbers."""
        self.assertEqual(sum_evens_and_odds([1, 3, 5, 7, 9]), {'evens': 0, 'odds': 25})

    def test_should_handle_all_even_numbers(self):
        """Test case with only even numbers."""
        self.assertEqual(sum_evens_and_odds([2, 4, 6, 8, 10]), {'evens': 30, 'odds': 0})

    def test_should_handle_negative_numbers(self):
        """Test case with negative even and odd numbers."""
        self.assertEqual(sum_evens_and_odds([-1, -2, -3, -4, -5]), {'evens': -6, 'odds': -9})

    def test_should_handle_mixed_positive_and_negative_numbers(self):
        """Test case with a mix of positive and negative even and odd numbers."""
        self.assertEqual(sum_evens_and_odds([-10, -5, 0, 3, 8]), {'evens': -2, 'odds': -2})

    def test_should_handle_zero(self):
        """Test case where the list contains only zero."""
        self.assertEqual(sum_evens_and_odds([0]), {'evens': 0, 'odds': 0})

    def test_should_handle_large_numbers(self):
        """Test case with very large numbers."""
        self.assertEqual(sum_evens_and_odds([10**6, 10**6 + 1]), {'evens': 10**6, 'odds': 10**6 + 1})

    def test_should_handle_single_even_number(self):
        """Test case with a single even number."""
        self.assertEqual(sum_evens_and_odds([2]), {'evens': 2, 'odds': 0})

    def test_should_handle_single_odd_number(self):
        """Test case with a single odd number."""
        self.assertEqual(sum_evens_and_odds([3]), {'evens': 0, 'odds': 3})

    def test_should_handle_repeated_numbers(self):
        """Test case with repeated numbers."""
        self.assertEqual(sum_evens_and_odds([2, 2, 2, 3, 3]), {'evens': 6, 'odds': 6})

    def test_should_handle_large_list(self):
        """Test case with a large list of sequential numbers."""
        self.assertEqual(sum_evens_and_odds(list(range(1, 101))), {'evens': 2550, 'odds': 2500})
