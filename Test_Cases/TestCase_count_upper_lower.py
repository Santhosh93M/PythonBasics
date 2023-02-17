import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.count_upper_lower import count_upper_lower

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count_upper_lower("Fly Until You Touch The Sky"),(6,21))
    def test_case2(self):
        self.assertEqual(count_upper_lower(""),(0,0))
