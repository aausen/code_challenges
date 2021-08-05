import unittest

def merge_lists(lst1, lst2):
    merged_list_size = len(lst1) + len(lst2)
    merged_list = [None] * merged_list_size

    current_idx_lst1 = 0
    current_idx_lst2 = 0 
    current_idx_merged = 0
    while current_idx_merged < merged_list_size:
        is_lst2_exhausted = current_idx_lst2 >= len(lst2)
        is_lst1_exhausted = current_idx_lst1 >= len(lst1)
       

        if (not is_lst2_exhausted and 
                (is_lst1_exhausted or 
                lst2[current_idx_lst2] < lst1[current_idx_lst1])):
        
            merged_list[current_idx_merged] = lst2[current_idx_lst2]
            current_idx_lst2 += 1
        else:
            merged_list[current_idx_merged] = lst1[current_idx_lst1]
            current_idx_lst1 += 1

        current_idx_merged += 1

    return merged_list

# Tests
class Test(unittest.TestCase):
    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([4, 5, 6], [])
        expected = [4, 5, 6]
        self.assertEqual(actual, expected)

    def test_both_lists_have_diff_nums(self):
        actual = merge_lists([1, 3, 4], [2, 5, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)
    
    def test_both_have_dif_len_lists(self):
        actual = merge_lists([1, 3, 4], [2, 5, 6, 7, 8, 9])
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)


    # take in two lists
    # look at each element to decide which is less
    # add the less one to the list
    # look for next less number
    # if one list runs out, append the rest of remaining list
    # merged_list = []
    # i = 0 
    # j = 0

    # for i in lst1:
    #     for j in lst2:
    #         if i < j:
    #             merged_list.append(i)
    #             i += 1
    #         if j < i:
    #             merged_list.append(j)
    #             j += 1

