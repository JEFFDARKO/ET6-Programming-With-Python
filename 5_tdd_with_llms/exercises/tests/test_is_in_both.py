#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_in_both function.
"""

import unittest
from ..is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """Test suite for the is_in_both function"""

    def test_item_in_both_lists(self):
        """Should return True because the string is in both lists"""
        self.assertEqual(is_in_both('welcome', ['add', 'welcome'], ['welcome', 'hello']), True)

    def test_item_in_one_list_only(self):
        """Should return False because the string is in only one list"""
        self.assertEqual(is_in_both('welcome', ['add', 'welcome'], ['hello', 'group']), False)

    def test_item_not_in_either_list(self):
        """Should return False because the string is not in either list"""
        self.assertEqual(is_in_both('missing', ['add', 'welcome'], ['hello', 'group']), False)

    def test_empty_lists(self):
        """Should return False because both lists are empty"""
        self.assertEqual(is_in_both('welcome', [], []), False)

    def test_empty_first_list(self):
        """Should return False because the first list is empty"""
        self.assertEqual(is_in_both('welcome', [], ['welcome', 'group']), False)

    def test_empty_second_list(self):
        """Should return False because the second list is empty"""
        self.assertEqual(is_in_both('welcome', ['add', 'welcome'], []), False)

    def test_case_sensitive_match(self):
        """Should return False because the match is case-sensitive"""
        self.assertEqual(is_in_both('Welcome', ['add', 'welcome'], ['welcome', 'hello']), False)

    def test_special_characters_in_string(self):
        """Should return True because the string with special characters matches in both lists"""
        self.assertEqual(is_in_both('group-7', ['group-7', 'welcome'], ['hello', 'group-7']), True)

    def test_spaces_in_string(self):
        """Should return True because the string with spaces matches in both lists"""
        self.assertEqual(is_in_both('group 7', ['group 7', 'welcome'], ['hello', 'group 7']), True)

    def test_non_string_items_in_lists(self):
        """Should raise AssertionError because the list contains non-string items"""
        with self.assertRaises(AssertionError):
            is_in_both('welcome', ['add', 123], ['welcome', True])

    def test_invalid_string_type(self):
        """Should raise AssertionError because the first argument is not a string"""
        with self.assertRaises(AssertionError):
            is_in_both(123, ['add', 'welcome'], ['welcome', 'hello'])

    def test_invalid_list1_type(self):
        """Should raise AssertionError because the first list is not a list"""
        with self.assertRaises(AssertionError):
            is_in_both('welcome', 'not_a_list', ['welcome', 'hello'])

    def test_invalid_list2_type(self):
        """Should raise AssertionError because the second list is not a list"""
        with self.assertRaises(AssertionError):
            is_in_both('welcome', ['add', 'welcome'], 'not_a_list')

    def test_all_elements_in_list1_not_strings(self):
        """Should raise AssertionError because the first list contains non-string items"""
        with self.assertRaises(AssertionError):
            is_in_both('welcome', [1, 2, 3], ['welcome', 'hello'])

    def test_all_elements_in_list2_not_strings(self):
        """Should raise AssertionError because the second list contains non-string items"""
        with self.assertRaises(AssertionError):
            is_in_both('welcome', ['add', 'welcome'], [True, None, 45.67])
