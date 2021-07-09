"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


from typing import Counter


def compress(string):
    """Return a compressed version of the given string."""
    # create a new string
    compressed_string=[]
    # Look at each char in string and compare to the next char
    first_char = string[0]
    counter = 0
    for char in string[1:]:
        if first_char == char:
            counter += 1
        else: 
            compressed_string.append(first_char)
            if counter > 1:
                compressed_string.append(str(counter))
                counter = 0
        first_char = char
    print("".join(compressed_string))
    # if followed by the same char, increment a count
    # else add the letter to the new string
    # print the new string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
