import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.largest_OddEven import large_odd_even

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(large_odd_even([12,45,32,33,67,98,11,1,2]),(98,67))
    def test_case2(self):
        self.assertEqual(large_odd_even([]),(0,0))
    def test_case3(self):
        self.assertEqual(large_odd_even([12,24,44]),(44,0))
