"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    # Create var for new list
    # create variable for current char
    # start counter
    # loop through each character in the string
    # if counter is equal to limit, send word to next line and reset counter
    # if in the middle of the word, send the whole word to the next line
    # join new list on line break
    # print resulting string
    
    new_lst = []
    current = ""
    char_count = 0
    for char in string:
        char_count += 1
        current = current + char
        print(current)
        if char_count == limit:
            new_lst.append(current)
            current = ""
            char_count = 0

    print(new_lst)
       
    
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
