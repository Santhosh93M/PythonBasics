import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.second_largest import second_largest

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(second_largest([12,45,23,555,67,111,78]),111)
    def test_case2(self):
        self.assertEqual(second_largest([12]),12)
    def test_case3(self):
        self.assertEqual(second_largest([-8,-45,-78,-1]),-8)
