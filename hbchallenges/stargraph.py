# problem from leetcode with Maura
import unittest
from unittest.case import TestCase

def findCenter(edges):
        seen = {}
        
        for edge in edges:
            for num in edge:
                if num in seen:
                    seen[num] += 1
                else:
                    seen[num] = 1
        for key in seen:
            if seen[key] > 1:
                return key

class Test(unittest.TestCase):

    def test_small_graph(self):
        edges = [[1, 2], [2, 3], [4, 2]]
        result = findCenter(edges)
        expected = 2
        self.assertEqual(result, expected)

    def test_med_graph(self):
        edges = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4]]
        result = findCenter(edges)
        expected = 4
        self.assertEqual(result, expected)

    def test_lg_graph(self):
        edges = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [7, 6], [8, 6], [9, 6]]
        result = findCenter(edges)
        expected = 6
        self.assertEqual(result, expected)

unittest.main(verbosity=2)