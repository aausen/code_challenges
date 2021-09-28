import unittest
def recursive_index(needle, haystack):

    def _recursive_index(needle, haystack, start):

        if start == len(haystack):
            return None
        if haystack[start] == needle:
            return start

        return _recursive_index(needle, haystack, start + 1)

    return _recursive_index(needle, haystack, 0)

def fit_to_width(string, limit):
    # split the list at white space to make list
    # pop last item out of the list
    # if item is less or equal to limit, 
    # check 
    # lines = list of strings
    # for line in lines
    # print(line)
    pass

class Test(unittest.TestCase):

    def test_in_haystack(self):
        result = recursive_index("hey", ["hey", "you", "there"])
        expected = 0
        self.assertEqual(result, expected)

    def test_not_in_haystack(self):
        result = recursive_index(3, [1, 4, 5, 6])
        expected = None
        self.assertEqual(result, expected)

    def test_short_list(self):
        result = recursive_index(4, [5, 4])
        expected = 1
        self.assertEqual(result, expected)

    def test_at_end(self):
        result = recursive_index(2, [5, 4, 6, 3, 5, 4, 5, 3, 2])
        expected = 8
        self.assertEqual(result, expected)

unittest.main(verbosity=2)