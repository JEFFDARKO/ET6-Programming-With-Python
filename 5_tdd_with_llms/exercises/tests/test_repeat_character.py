#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import unittest

from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    """"""

    # Standard test cases
    def test_omnia_m_7(self):
          "It should repeat 'm' 7 times in Omina"
          self.assertEqual(repeat_character('omnia', 'm', 7), 'ommmmmmmnia')
          
          
    def test_Jola_Moses_s_2(self):
          "It should repeat 's' 2 times in Jola Moses"
          self.assertEqual(repeat_character('Jola-Moses', 's', 2), 'Jola-Mossess')
  
