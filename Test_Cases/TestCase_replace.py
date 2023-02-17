import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.replace_char import replace

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(replace("saaaan"),"s$$$$n")
    def test_case2(self):
        self.assertEqual(replace("hello"),"hello")
    def test_case3(self):
        self.assertEqual(replace(""),"")
