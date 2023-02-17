import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.factorial import factorial

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(factorial(0),1)
    def test_case2(self):
        self.assertEqual(factorial(-3),0)
    def test_case3(self):
        self.assertEqual(factorial(5),120)
