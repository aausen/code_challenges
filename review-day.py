import unittest

def print_every_other(given_str):
    even = []
    odd = []
    for idx, char in enumerate(given_str):
        if idx % 2 == 0:
            even.append(char)
        else:
            odd.append(char) 
    new_even = "".join(even)
    new_odd = "".join(odd)
    return f"{new_even} {new_odd}"

# Tests

class Tests(unittest.TestCase):

    def test_one_word(self):
        given_str = "apple"
        result = print_every_other(given_str)
        expected = "ape pl"
        self.assertEqual(result, expected)

    def test_no_word(self):
        given_str = ""
        result = print_every_other(given_str)
        expected = " "
        self.assertEqual(result, expected)

    def test_one_char(self):
        given_str = "a"
        result = print_every_other(given_str)
        expected = "a "
        self.assertEqual(result, expected)

unittest.main(verbosity=2)


#Hacker rank solution online suggestion
# num_test_cases = int(input())

# for i in range(num_test_cases):
#     test_string = input()
#     even_idx_char = ''
#     odd_idx_char = ''

#     for j in range(len(test_string)):
#         if j % 2 == 0:
#             even_idx_char += test_string[j]
#         else:
#             odd_idx_char += test_string[j]

#     print(f"{even_idx_char} {odd_idx_char}")
