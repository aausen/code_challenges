import unittest
from unittest import result
from unittest.case import expectedFailure

def is_anagram_of_palendrome(word):

    seen = {}

    for char in word:
        count = seen.get(char, 0)
        seen[char] = count + 1

    seen_an_odd = False

    for count in seen.values():
        if count % 2 != 0:
            if seen_an_odd:
                return False
            seen_an_odd = True
    return True

class Test(unittest.TestCase):

    def test_anagram(self):
        result = is_anagram_of_palendrome("omm")
        expected = True
        self.assertEqual(result, expected)

    def test_not_anagram(self):
        result = is_anagram_of_palendrome("hello")
        expected = False
        self.assertEqual(result, expected)

    def test_long_word(self):
        result = is_anagram_of_palendrome("tacocat")
        expected = True
        self.assertEqual(result, expected)

    def test_out_of_order(self):
        result = is_anagram_of_palendrome("ccivi")
        expected = True
        self.assertEqual(result, expected)

    def test_long_not_anagram(self):
        result = is_anagram_of_palendrome("ababadc")
        expected = False
        self.assertEqual(result, expected)


unittest.main(verbosity=2)