import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_list_nonetype(self):
        """tests max_list function if the list is nonetype"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    
    def test_max_list_iter_list_empty(self):
        """tests max_list function if the list is empty"""
        tlist = []
        self.assertEqual(max_list_iter([]),None)

    def test_max_list_iter_list_find_max(self):
        """tests max_list function to find the max"""
        self.assertEqual(max_list_iter([1,2,3]),3)
        self.assertEqual(max_list_iter([1,3,2]),3)
        self.assertEqual(max_list_iter([3,1,2]),3)

    def test_reverse_rec_list_nonetype(self):
        """tests reverse_rec function if the list is nonetype"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_reverse_list(self):
        """tests reverse_rec function to see if it reverses a list"""
        self.assertEqual(reverse_rec([3,1,2]),[2,1,3])
        self.assertEqual(reverse_rec([3,1,2,4]),[4,2,1,3])
        self.assertEqual(reverse_rec([3,1,2,5,2]),[2,5,2,1,3])

    def test_bin_search_find_value(self):
        """tests bin_search to find value in a sorted list"""
        tlist = [0,1,2,3,4,5,6,7,8,9,10]
        low, high = 0, len(tlist)-1
        self.assertEqual(bin_search(4, low, high, tlist), 4)
        self.assertEqual(bin_search(0, low, high, tlist), 0)
        self.assertEqual(bin_search(10, low, high, tlist), 10)
    
    def test_bin_search_list_nonetype(self):
        tlist = None
        low, high = 0, 10
        with self.assertRaises(ValueError):
            bin_search(3, low, high, tlist)

    def test_bin_search_val_nonexistent(self):
        tlist = [0,1,3,4,5,6,8]
        low, high = 0, len(tlist)-1
        self.assertEqual(bin_search(7, low, high, tlist), None)
        self.assertEqual(bin_search(2, low, high, tlist), None)

if __name__ == "__main__":
        unittest.main()

    
