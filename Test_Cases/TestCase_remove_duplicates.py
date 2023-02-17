import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.Remove_Duplicates import remove_duplicates

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(remove_duplicates( [1,1,13,13, 21, 23, 34, 45, 45, 67, 67, 78, 90]),[1,13,21,23,34,45,67,78,90])
    def test_case2(self):
        self.assertEqual(remove_duplicates([]),[])
    def test_case3(self):
        self.assertEqual(remove_duplicates([1,1,1,1,1]),[1])
