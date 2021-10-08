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
    """Replace white space with "%20"."""
    new_char_str = char_string.strip()
    char_list = list(new_char_str)
    for i, char in enumerate(char_list):
        if char == " ":
            char_list[i] = "%20"
    new_url = "".join(char_list)
    return new_url

#______________________1.4________________________________#
def is_palendrome_permutaion(stringA):
    """Check if string is permutation of a palendrome."""

    unpaired_char = set()

    for char in stringA.replace(" ", ""):
        if char in unpaired_char:
            unpaired_char.remove(char)
        else:
            unpaired_char.add(char)

    return len(unpaired_char) <= 1



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
#___________________1.3____________________#
    def test_john_smith(self):
        actual = urlify("Mr John Smith    ", 13)
        expected = "Mr%20John%20Smith"
        self.assertEqual(actual, expected)

    def test_short_phrase(self):
        actual = urlify("hello you  ", 9)
        expected = "hello%20you"
        self.assertEqual(actual, expected)
#__________________1.4_______________________#
    def test_is_palendrome(self):
        actual = is_palendrome_permutaion("toac tca")
        expected = True
        self.assertEqual(actual, expected)
    
    def test_is_not_palendrome(self):
        actual = is_palendrome_permutaion("this is")
        expected = False
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)