import unittest
import sys
sys.path.append("D:/Documents/python")

from programs.Adding_two_list import concat

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(concat([1,2,3],[4,5,6]),[1,2,3,4,5,6])
    def test_case2(self):
        self.assertEqual(concat([],[]),[])



