"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    pointer_a = 0
    pointer_b = 0
    merged_list = []

    while pointer_a < len(a) and pointer_b < len(b):
        if a[pointer_a] < b[pointer_b]:
            merged_list.append(a[pointer_a])
            pointer_a += 1
        else:
            merged_list.append(b[pointer_b])
            pointer_b += 1

    merged_list.extend(a[pointer_a:])
    merged_list.extend(b[pointer_b:])

    return merged_list
    
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
