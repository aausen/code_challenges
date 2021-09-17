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
    # loop through string
    # when index count == limit, break
    # if chr is not a space, find a space
    # print the string
    # my first thoughts

    # i = 0
    # new_string = []
    # for char in string:
    #     new_string.append(char)
    #     i += 1
    #     if i == limit:
    #         if char == " ":
    #             print("".join(new_string))
    #             i = 0
    #             new_string = []
    #         if char != " ":
    #             pass

    tokens = list(reversed(string.split()))
    lines = []

    current_line = []
    while tokens:
        word = tokens[-1]
        if len(" ".join(current_line + [word])) <= limit:
            current_line.append(tokens.pop())
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = []

    lines.append(" ".join(current_line))

    for line in lines:
        print(line)

# in this solution we start by creating a stack. We do this to see if the last word will fit on the current line
# if not, it makes it easy to move that to the next line instead.
# We use a while loop to loop through the list until the list is depleated (since we are popping them)
# inside the loop, we start by def a var word to start with (the last word in the list(formerly the first))
# 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
