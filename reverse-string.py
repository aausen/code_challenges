import unittest
# the function will take in a list
# create a new list to append to 
# look at each element
# append to the front of the list
# time O(n), space O(n**2)
# def reverse_str(string_list):
#     reversed_list = []
#     for el in string_list:
#         reversed_list.insert(0, el)
#     return reversed_list

# print(reverse_str(['e', 'i', 'n', 'n', 'a']))

def reverse(list_of_chars):

    left_index = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]

        left_index += 1
        right_index -= 1
    
# reverse(['e', 'i', 'n', 'n', 'a'])

# Tests

class Tests(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_one_char(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_many_chars(self):
        list_of_chars = ['e', 'i', 'n', 'n', 'a']
        reverse(list_of_chars)
        expected = ['a', 'n', 'n', 'i', 'e']
        self.assertEqual(list_of_chars, expected)

unittest.main(verbosity=2)