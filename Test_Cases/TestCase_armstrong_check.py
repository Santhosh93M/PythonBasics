import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.armstrong_check import check_armstrong

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(check_armstrong(153),True)
    def test_case2(self):
        self.assertEqual(check_armstrong(90),False)
    def test_case3(self):
        self.assertEqual(check_armstrong(-1),False)
