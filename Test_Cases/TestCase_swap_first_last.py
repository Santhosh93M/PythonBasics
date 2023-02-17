import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.swap_firstlast_list import swap_first_last

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(swap_first_last([-1,-2,-3,2,3,4,5,6,7]),[7,-2,-3,2,3,4,5,6,-1])
    def test_case2(self):
        self.assertEqual(swap_first_last([12]),[12])
    def test_case3(self):
        self.assertEqual(swap_first_last([-8,-45,-78,-4]),[-4,-45,-78,-8])
