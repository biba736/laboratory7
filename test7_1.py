import unittest
from lab71 import binSearch

class TestBinSearch(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(binSearch([1, 3, 5, 7, 9], 5), [5])
        self.assertEqual(binSearch([1, 3, 5, 7, 9], 3), [5, 1, 3])

    def test_edge_cases(self):
        self.assertEqual(binSearch([1, 3, 5, 7, 9], 1), [5, 1])
        self.assertEqual(binSearch([1, 3, 5, 7, 9], 9), [5, 7, 9])

    def test_not_found(self):
        self.assertEqual(binSearch([1, 3, 5, 7, 9], 4), [5, 1, 3])
        self.assertEqual(binSearch([1, 3, 5, 7, 9], 8), [5, 7, 9])

    def test_empty_array(self):
        self.assertEqual(binSearch([], 5), [])

    def test_out_of_bounds(self):
        self.assertIsNone(binSearch([1, 3, 5, 7, 9], 0))
        self.assertIsNone(binSearch([1, 3, 5, 7, 9], 10))

    def test_even_length(self):
        self.assertEqual(binSearch([1, 3, 5, 7], 3), [3])
        self.assertEqual(binSearch([1, 3, 5, 7], 5), [3, 5])
