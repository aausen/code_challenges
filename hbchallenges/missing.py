"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
# sort the given list
    # sorted_nums = sorted(nums)
    # for i, num in enumerate(sorted_nums):
    #     if num < max_num:
    #         if num(i + 1) != num[i] + 1:
    #             return num[i + 1]
            
 

    seen = [False] * max_num 
    


    
# look at each number in the given list
# number less than max number
# start at idx 0 
# compare idx 0 to idx 1
#    if idx 1 is equal to idx 0 plus one, keep looping
#    else return the given value    


# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASS. NICELY DONE!\n")
