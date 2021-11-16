import unittest

def get_permutations(string):

    if len(string) < 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations_of_all_chars_execpt_last = get_permutations(all_chars_except_last)

    permutations = set()

    for permutation_of_all_chars_except_last in permutations_of_all_chars_execpt_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[position:]
                + last_char
                + permutation_of_all_chars_except_last[:position]
            )

            permutations.add(permutation)

    return permutations

class Test(unittest.TestCase):

    def test_empty_string(self):
        result = get_permutations("")
        expected = set([""])
        self.assertEqual(result, expected)

    def test_one_letter(self):
        result = get_permutations("a")
        expected = set(["a"])
        self.assertEqual(result, expected)

    def test_two_letters(self):
        result = get_permutations("at")
        expected = set(["at", "ta"])
        self.assertEqual(result, expected)

    def test_one_word(self):
        result = get_permutations("cat")
        expected = set(["cat", "cta", "tca", "act", "atc", "tac"])
        self.assertEqual(result, expected)

unittest.main(verbosity=2)