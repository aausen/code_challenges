import unittest

## Reverse string in place 8/16
def reverse(list_of_char):
    left_index = 0 
    right_index = len(list_of_char) - 1

    while left_index < right_index:
        list_of_char[left_index], list_of_char[right_index] = \
            list_of_char[right_index], list_of_char[left_index]

        left_index += 1
        right_index -= 1

# Tests for reverse

class Tests(unittest.TestCase):

    def test_even_list(self):
        list_of_char = ['a', 'b', 'c', 'd']
        reverse(list_of_char)
        expected = ['d', 'c', 'b', 'a']
        self.assertEqual(list_of_char, expected)

    def test_empty_list(self):
        list_of_char = []
        reverse(list_of_char)
        expected = []
        self.assertEqual(list_of_char, expected)

    def test_odd_list(self):
        list_of_char = ['a', 'b', 'c']
        reverse(list_of_char)
        expected = ['c', 'b', 'a']
        self.assertEqual(list_of_char, expected)
    
    def test_single_character(self):
        list_of_char = ['a']
        reverse(list_of_char)
        expected = ['a']
        self.assertEqual(list_of_char, expected)

unittest.main(verbosity=2)