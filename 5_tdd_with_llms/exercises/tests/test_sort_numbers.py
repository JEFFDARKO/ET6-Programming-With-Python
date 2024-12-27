#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import unittest
from ..sort_numbers import sort_numbers

class TestSortNumbers(unittest.TestCase):
    """Test suite for sort_numbers function"""

    # Test with an empty list
    def test_example_with_empty_list(self):
        "This should return an empty list"
        self.assertEqual(sort_numbers([]), [])

    # Test with a list that is already sorted
    def test_with_sorted_list(self):
        "This should return the same sorted list"
        self.assertEqual(sort_numbers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    # Test with a list in reverse order
    def test_with_reversed_list(self):
        "This should return the sorted list"
        self.assertEqual(sort_numbers([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Test with a list containing negative numbers
    def test_with_negative_numbers(self):
        "This should correctly sort negative numbers"
        self.assertEqual(sort_numbers([10, -1, 5, -3, 0]), [-3, -1, 0, 5, 10])

    # Test with duplicates
    def test_with_duplicates(self):
        "This should handle duplicate numbers correctly"
        self.assertEqual(sort_numbers([4, 2, 4, 3, 2]), [2, 2, 3, 4, 4])

    # Test with a single element
    def test_with_single_element(self):
        "This should return the same list with one element"
        self.assertEqual(sort_numbers([42]), [42])

    # Test with large numbers
    def test_with_large_numbers(self):
        "This should correctly handle large numbers"
        self.assertEqual(sort_numbers([999999999, -999999999, 0]), [-999999999, 0, 999999999])

    # defensive assertion tests
    def test_if_input_is_a_string_not_list(self):
        "It should raise an error if list_of_numbers is a string"
        with self.assertRaises(AssertionError):
            sort_numbers('three')

    #input is an integer, not a list
    def test_if_input_is_an_integer_not_list(self):
        "It should raise an error if list_of_numbers is an integer"
        with self.assertRaises(AssertionError):
            sort_numbers(123)

    #input is None
    def test_if_input_is_none(self):
        "It should raise an error if list_of_numbers is None"
        with self.assertRaises(AssertionError):
            sort_numbers(None)

    # Test with floats
    def test_with_floating_point_numbers(self):
        "This should correctly sort floating-point numbers"
        self.assertEqual(sort_numbers([3.14, 2.71, -1.0, 0.0]), [-1.0, 0.0, 2.71, 3.14])

    # Test ints & floats
    def test_with_mixed_numbers(self):
        "This should correctly sort mixed integers and floating-point numbers"
        self.assertEqual(sort_numbers([3, 2.71, 5, -1.0]), [-1.0, 2.71, 3, 5])

    def test_custom_input(self):
        "This should sort the custom test input"
        self.assertEqual(sort_numbers([7, 3, 9, 2, 8, 1, 6, 4, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
