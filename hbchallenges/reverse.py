"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
# base case empty string
# need to remove a letter from the string each time
# add back a letter first in, last out (stack?)
# progress => 
# make empty list

    print("*"*20, "This is the beginning!")
    print("astring:", astring)
    astring_lst = list(astring)
    print("astring_lst", astring_lst)
    new_lst = []
    print("new_lst: ", new_lst)
    if astring_lst == []:
        return 

    else:
        end_char = astring_lst.pop()
        # astring_lst.remove(end_char)
        print("end_char:", end_char)
        print("astring_lst after pop:", astring_lst)
        new_lst.append(end_char)
        rev_string("".join(new_lst))

def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """

    # START SOLUTION

    if len(astring) < 2:
        return astring

    return astring[-1] + rev_string(astring[:-1])

# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
