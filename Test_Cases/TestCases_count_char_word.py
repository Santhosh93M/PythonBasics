import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.count_char_words import count_char_word

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count_char_word("fly until you touch the sky"),(6,22))
    def test_case2(self):
        self.assertEqual(count_char_word(""),(0,0))
