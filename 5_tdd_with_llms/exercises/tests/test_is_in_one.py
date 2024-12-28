#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_in_one function.
"""

import unittest

from ..is_in_one import is_in_one

class TestIsInOne(unittest.TestCase):
  """Tests for is_in_one function"""

  def test_should_return_in_one_test(self):
    """Test case where string is in only one list."""
    self.assertEqual(is_in_one('welcome', ['add', 'welcome', 'group 7'], ['run', 'hello', 'group']), True)

  def test_should_return_not_in_either_list(self):
    """Test case where string is in neither list."""
    self.assertEqual(is_in_one('absent', ['alpha', 'beta'], ['gamma', 'delta']), False)

  def test_should_return_in_both_lists(self):
    """Test case where string is present in both lists."""
    self.assertEqual(is_in_one('shared', ['shared', 'alpha'], ['shared', 'beta']), False)

  def test_should_return_empty_lists(self):
    """Test case where both lists are empty."""
    self.assertEqual(is_in_one('nothing', [], []), False)

  def test_should_return_in_first_list_only(self):
    """Test case where string is in the first list only."""
    self.assertEqual(is_in_one('first_only', ['first_only', 'alpha'], ['beta', 'gamma']), True)

  def test_should_return_in_second_list_only(self):
    """Test case where string is in the second list only."""
    self.assertEqual(is_in_one('second_only', ['alpha', 'beta'], ['second_only', 'gamma']), True)

  def test_should_return_case_sensitive_check(self):
    """Test case for case sensitivity."""
    self.assertEqual(is_in_one('Case', ['Case', 'alpha'], ['case', 'gamma']), True)

  def test_should_raise_assertion_for_non_string_element(self):
    """Test case where a non-string element is present in the lists."""
    with self.assertRaises(AssertionError):
        is_in_one('check', ['alpha', 123], ['beta', 'gamma'])

  def test_should_raise_assertion_for_non_list_argument(self):
    """Test case where an argument is not a list."""
    with self.assertRaises(AssertionError):
        is_in_one('check', 'not a list', ['beta', 'gamma'])

  def test_should_return_in_first_list_duplicates(self):
    """Test case where the string is duplicated in the first list only."""
    self.assertEqual(is_in_one('dup', ['dup', 'dup'], ['alpha', 'beta']), True)
