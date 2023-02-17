import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.remove_odd_indexed_char import remove_odd_indexed

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(remove_odd_indexed("santhosh"),"snhs")
    def test_case2(self):
        self.assertEqual(remove_odd_indexed("s"),"s")
    def test_case3(self):
        self.assertEqual(remove_odd_indexed("s-a-n-t-h-o-s-h"),"santhosh")
