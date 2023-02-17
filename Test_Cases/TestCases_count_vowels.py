import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.count_vowels import count_vowels

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count_vowels("Fly Until You Touch The Sky"),6)
    def test_case2(self):
        self.assertEqual(count_vowels(""),0)
    def test_case3(self):
        self.assertEqual(count_vowels("hhhhh"),0)
