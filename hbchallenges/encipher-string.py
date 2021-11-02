"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""

    encoded_string = ""
    for char in txt:
        char = ord(char)

        if 65 <= char <= 90:
            new_char = char + shift
            if new_char > 90:
                new_char -= 26
            new_char = chr(new_char)
            encoded_string += new_char

        elif 97 <= char <= 122:
            new_char = char + shift
            if new_char > 122:
                new_char -= 26
            new_char = chr(new_char)
            encoded_string += new_char
        
        else:
            char = chr(char)
            encoded_string += char
    return encoded_string

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
