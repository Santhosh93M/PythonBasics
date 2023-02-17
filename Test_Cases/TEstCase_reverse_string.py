import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.Reverse_string import reverse_string

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(reverse_string("saaaan"),"naaaas")
    def test_case2(self):
        self.assertEqual(reverse_string("hello"),"olleh")
    def test_case3(self):
        self.assertEqual(reverse_string(" ")," ")
