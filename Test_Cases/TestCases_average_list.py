import unittest

import sys
sys.path.append("D:/Documents/python")

from programs.average_list import average

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(average([4,5,6,7]),5)
    def test_case2(self):
        self.assertEqual(average([]),0)
