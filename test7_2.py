import unittest
from lab72 import interpolSearch

class TestBinSearch(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(interpolSearch([1, 3, 5, 7, 9], 5), [5])
        self.assertEqual(interpolSearch([1, 3, 5, 7, 9], 3), [3])

    def test_edge_cases(self):
        self.assertEqual(interpolSearch([1, 3, 5, 7, 9], 1), [1])
        self.assertEqual(interpolSearch([1, 3, 5, 7, 9], 9), [9])

    def test_not_found(self):
        self.assertEqual(interpolSearch([1, 3, 5, 7, 9], 4), [5])
        self.assertEqual(interpolSearch([1, 3, 5, 7, 9], 8), [9])

    def test_empty_array(self):
        self.assertEqual(interpolSearch([], 5), [])

    def test_out_of_bounds(self):
        self.assertIsNone(interpolSearch([1, 3, 5, 7, 9], 0))
        self.assertIsNone(interpolSearch([1, 3, 5, 7, 9], 10))