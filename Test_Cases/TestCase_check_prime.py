import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.prime_check import check_prime

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(check_prime(1),False)
    def test_case2(self):
        self.assertEqual(check_prime(-3),False)
    def test_case3(self):
        self.assertEqual(check_prime(7),True)
