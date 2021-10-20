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

#____________________________1.5______________________________#
def one_away(str1, str2):
    len_difference = len(str1) - len(str2)
    if len_difference > 1:
        return False
    elif len_difference == 0:
        diffrence = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diffrence += 1
                if diffrence > 1:
                    return False
        return True
    else:
        if abs(len(str1) > len(str2)):
            longer, shorter = str1, str2
        else:
            longer, shorter = str2, str1
        move = 0
        for i in range(len(shorter)):
            if shorter[i] != longer[i + move]:
                if move or (shorter[i] != longer[i + 1]):
                    return False
                move = 1
        return True

#_____________________1.6________________________#
def string_compression(string1):
    # count
    # new string
    # loop through string starting at 1
    # if previous char is the same as current, add to count
    # when char changes, add char[i - 1] with count to new string
    # reset the count
    # compare if len on new string is less than given string
    # if so return new string
    # otherwise return original string

    count = 0
    new_string = ""

    for i in range(len(string1)):
        if string1[i] == string1[i - 1]:
            count += 0
        else:
            new_string = new_string + string[i - 1] + count
            count = 0
    if len(new_string) < string1:
        return new_string
    else:
        return string1

# needs to be fixed!

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

#_________________1.5_____________________________#
    def test_remove_one_letter(self):
        actual = one_away("pale", "ple")
        expected = True
        self.assertEqual(actual, expected)

    def test_insert_one_letter(self):
        actual = one_away("pale", "pales")
        expected = True
        self.assertEqual(actual, expected)

    def test_replace_one_letter(self):
        actual = one_away("bale", "pale")
        expected = True
        self.assertEqual(actual, expected)

    def test_not_one_away(self):
        actual = one_away("bake", "pale")
        expected = False
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)