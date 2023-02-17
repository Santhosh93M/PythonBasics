import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.Longest_word import longest_word

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(longest_word(["hello" ,"world","think","first", "before", "you", "do"]),6)
    def test_case2(self):
        self.assertEqual(longest_word([]),0)
    def test_case3(self):
        self.assertEqual(longest_word(["i"]),1)
