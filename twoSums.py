import unittest

def twoSums(target, nums):
    seen = {}

    for i, b in enumerate(nums):
        a = target - b
        if a in seen:
           return [seen[a], i]
        else:
            seen[b] = i  

class Test(unittest.TestCase):

    def test_two_nums(self):
        target = 5
        nums = [2, 3]
        result = twoSums(target, nums)
        expected = [0, 1]
        self.assertEqual(result, expected)

    def test_lots_of_nums(self):
        target = 10
        nums = [1, 4, 5, 11, 6, 3]
        result = twoSums(target, nums)
        expected = [1, 4]
        self.assertEqual(result, expected)

    def test_many_nums(self):
        target = 3
        nums = [4, 5, 8, 3, 7, 1, 2]
        result = twoSums(target, nums)
        expected = [5, 6]
        self.assertEqual(result, expected)

unittest.main(verbosity=2)