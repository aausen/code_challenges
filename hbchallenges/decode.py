"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(s):
    """Decode a string."""

    word =  ""
    i = 0

    while i < len(s):
        num_to_skip = int(s[i])
        i += num_to_skip + 1

        word += s[i]

        i += 1

    return word

# for this challenge we first set a variable to an empty
# string that we will return at the end
# we set i equal to 0 to keep track of the index
# use a while loop to loop through the given string
# to figure out how many to skip, we look at the string at 
# i and turn that into an integer
# we then add it to i plus one to get to the letter we need
# to decode the message. 
# add that letter to our new string
# then increment i by 1 to find where the next nubmer to skip is
# return the decripted word in the end

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n")
