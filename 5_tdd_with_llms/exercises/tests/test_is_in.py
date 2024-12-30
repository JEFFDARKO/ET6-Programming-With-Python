#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_in function.
"""

import unittest

from ..is_in import is_in

class TestIsIn(unittest.TestCase):
    """Tests for the is_in function"""

    def test_should_return_in_both_lists(self):
        """Test case where string is in both lists."""
        self.assertEqual(is_in('welcome', ['add', 'welcome', 'group 7'], ['welcome', 'hello', 'group']), True)

    def test_should_return_not_in_either_list(self):
        """Test case where string is in neither list."""
        self.assertEqual(is_in('absent', ['alpha', 'beta'], ['gamma', 'delta']), False)

    def test_should_return_empty_lists(self):
        """Test case where both lists are empty."""
        self.assertEqual(is_in('nothing', [], []), False)

    def test_should_return_in_first_list_only(self):
        """Test case where string is in the first list only."""
        self.assertEqual(is_in('first_only', ['first_only', 'alpha'], ['beta', 'gamma']), True)

    def test_should_return_in_second_list_only(self):
        """Test case where string is in the second list only."""
        self.assertEqual(is_in('second_only', ['alpha', 'beta'], ['second_only', 'gamma']), True)

    def test_should_handle_case_sensitivity(self):
        """Test case for case sensitivity."""
        self.assertEqual(is_in('Case', ['Case', 'alpha'], ['case', 'gamma']), True)

    def test_should_raise_assertion_for_non_string_element(self):
        """Test case where a non-string element is present in the lists."""
        with self.assertRaises(AssertionError):
            is_in('check', ['alpha', 123], ['beta', 'gamma'])

    def test_should_raise_assertion_for_non_list_argument(self):
        """Test case where an argument is not a list."""
        with self.assertRaises(AssertionError):
            is_in('check', 'not a list', ['beta', 'gamma'])

    def test_should_return_in_first_list_duplicates(self):
        """Test case where the string is duplicated in the first list"""
        self.assertEqual(is_in('dup', ['dup', 'dup'], ['alpha', 'beta']), True)
