import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.replace_spacewith_hyphen import replace_spaceTo_hyphen

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(replace_spaceTo_hyphen("sa aa an"),"sa-aa-an")
    def test_case2(self):
        self.assertEqual(replace_spaceTo_hyphen("hello  "),"hello--")
    def test_case3(self):
        self.assertEqual(replace_spaceTo_hyphen("   "),"---")
