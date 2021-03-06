"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""
    nums = str(num)
    list_nums = list(nums)
    left_index = 0
    right_index = len(list_nums) - 1

    while left_index < right_index:
        list_nums[left_index], list_nums[right_index] = list_nums[right_index], list_nums[left_index]
        left_index += 1
        right_index -= 1

    
    for char in list_nums:
        print(char)

# better answer:

# def print_digits(num):
#     while num:
#         next_digit = num % 10
#         print(next_digit)
#         num = (num- next_digit) // 10

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
