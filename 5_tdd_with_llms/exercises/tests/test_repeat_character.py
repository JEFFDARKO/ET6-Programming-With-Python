#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import unittest

from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    """"""

    # Standard test cases
    def test_empty_string(self):
      "it should return an empty if you pass an empty string"
      self.assertEqual(repeat_character('', 'm', 99999999), '')
      
      
      def test_case_sensitive_upper_text(self):
        "it should return the same string with """
        self.assertEqual(repeat_character('Agabani', 'a', 0), 'gbni')
      
    def test_repeat_character_seven_times(self):
          "It should repeat 'm' 7 times in Omina"
          self.assertEqual(repeat_character('omnia', 'm', 7), 'ommmmmmmnia')
          
          
    def test_with_more_than_one(self):
          "It should repeat 's' 2 times in Jola Moses"
          self.assertEqual(repeat_character('Jola-Moses', 's', 2), 'Jola-Mossess')
          
    def test_defensive_check_for_negative_repetitions(self):
      "It should raise an error if the repetition is less than 0"
      with self.assertRaises(AssertionError):
        repeat_character('Agabani', "A", -2)
