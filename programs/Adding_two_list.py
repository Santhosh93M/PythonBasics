import unittest
lst1 = [23,45,67,78,34,21]
lst2 = [13,45,67,1,90]
def concat(lst1,lst2):
    lst = lst1+lst2
    lst.sort()
    return lst

class Testaddlist(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(concat([1,2,3],[4,5,6]),[1,3,4,5,6])




