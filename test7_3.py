import unittest
from lab73 import fibSearch

class TestBinSearch(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(fibSearch([1, 3, 5, 7, 9], 5), [3, 5])
        self.assertEqual(fibSearch([1, 3, 5, 7, 9], 3), [3])

    def test_edge_cases(self):
        self.assertEqual(fibSearch([1, 3, 5, 7, 9], 1), [3, 1])
        self.assertEqual(fibSearch([1, 3, 5, 7, 9], 9), [3, 5, 7, 9])

    def test_not_found(self):
        self.assertEqual(fibSearch([1, 3, 5, 7, 9], 4), [3, 5, 5])
        self.assertEqual(fibSearch([1, 3, 5, 7, 9], 8), [3, 5, 7, 9])

    def test_empty_array(self):
        self.assertEqual(fibSearch([], 5), [])

    def test_out_of_bounds(self):
        self.assertIsNone(fibSearch([1, 3, 5, 7, 9], 0))
        self.assertIsNone(fibSearch([1, 3, 5, 7, 9], 10))