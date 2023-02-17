import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.maximum_list import maximum_element

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(maximum_element([12,45,23,555,67,111,78]),555)
    def test_case2(self):
        self.assertEqual(maximum_element([12]),12)
    def test_case3(self):
        self.assertEqual(maximum_element([-8,-45,-78,-1]),-1)
