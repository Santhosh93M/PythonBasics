import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.Polindrome_string import Ispolindrome

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(Ispolindrome("amma"),True)
    def test_case2(self):
        self.assertEqual(Ispolindrome("hello"),False)
    def test_case3(self):
        self.assertEqual(Ispolindrome(""),True)
