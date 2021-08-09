import unittest
from unittest import result

def has_palendrome_permutation(is_string):
    unpaired_chars = set()

    for char in is_string:
        if char in unpaired_chars:
           unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return len(unpaired_chars) <= 1

# Tests

class Test(unittest.TestCase):
    def test_is_palendrome(self):
        result = has_palendrome_permutation("civic")
        self.assertTrue(result)

    def test_is_not_palendrome(self):
        result = has_palendrome_permutation("civil")
        self.assertFalse(result)

    def test_is_palendrome_mixed_up(self):
        result = has_palendrome_permutation("iivcc")
        self.assertTrue(result)

    def test_empty_string(self):
        result = has_palendrome_permutation("")
        self.assertTrue(result)

    def test_one_char(self):
        result = has_palendrome_permutation("a")
        self.assertTrue(result)
        
unittest.main(verbosity=2)