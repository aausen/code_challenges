import unittest
"""A file for chapter 1 questions. Arrays and Strings."""

#____________________1.1___________________________#
def unique_char(string):
    sorted_str = sorted(string)

    for i in range(len(string) -1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    return True

#_____________________1.2_______________________________#
def is_permutation(first, second):
    sorted_first = sorted(first)
    sorted_second = sorted(second)

    if sorted_first == sorted_second:
        return True
    return False

#______________________1.3______________________________#
def urlify(char_string, char_len):
    char_list = list(char_string)
    print("before", char_list)
    for char in char_list:
        if char == " ":
            char_list[char] == "%20"
    print("after", char_list)



class Tests(unittest.TestCase):

    #______________1.1_____________________#

    def test_no_char(self):
        actual = unique_char("")
        expected = True
        self.assertEqual(actual, expected)

    def test_one_char(self):
        actual = unique_char("a")
        expected = True
        self.assertEqual(actual, expected)

    def test_repeated_char(self):
        actual = unique_char("ababa")
        expected = False
        self.assertEqual(actual, expected)

    def test_two_char(self):
        actual = unique_char("ab")
        expected = True
        self.assertEqual(actual, expected)

    def test_two_dif_char(self):
        actual = unique_char("cc")
        expected = False
        self.assertEqual(actual, expected)

    def test_many_char(self):
        actual = unique_char("nancyhall")
        expected = False
        self.assertEqual(actual, expected)

#________________1.2__________________#

    def test_same_word(self):
        actual = is_permutation("hi", "hi")
        expected = True
        self.assertEqual(actual, expected)

    def test_no_permutation(self):
        actual = is_permutation("yes", "no")
        expected = False
        self.assertEqual(actual, expected)

    def test_some_letters_same(self):
        actual = is_permutation("hello", "lo")
        expected = False
        self.assertEqual(actual, expected)

    def test_contains_permutation(self):
        actual = is_permutation("foot", "toof")
        expected = True
        self.assertEqual(actual, expected)




unittest.main(verbosity=2)