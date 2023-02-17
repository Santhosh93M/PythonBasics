import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.sumOf_pos_neg import sumOf

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(sumOf([-1,-2,-3,2,3,4,5,6,7]),(-6,12,15))
    def test_case2(self):
        self.assertEqual(sumOf([12]),(0,12,0))
    def test_case3(self):
        self.assertEqual(sumOf([-8,-45,-78,-4]),(-135,0,0))
