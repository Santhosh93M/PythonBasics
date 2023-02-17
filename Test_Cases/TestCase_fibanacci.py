import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.fibanacci import fibanacci

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(fibanacci(3),2)
    def test_case2(self):
        self.assertEqual(fibanacci(-2),0)
    def test_case3(self):
        self.assertEqual(fibanacci(8),21)

    
