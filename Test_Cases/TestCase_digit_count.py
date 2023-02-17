import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.digit_sum import digit_sum

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(digit_sum(12345),15)
    def test_case2(self):
        self.assertEqual(digit_sum(8),8)
    def test_case3(self):
        self.assertEqual(digit_sum(0),0)
