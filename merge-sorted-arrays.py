def merge_lists(lst1, lst2):
    merged_list_size = len(lst1) + len(lst2)
    merged_list = [None] * merged_list_size

    current_idx_lst1 = 0
    current_idx_lst2 = 0 
    current_idx_merged = 0
    while current_idx_merged < merged_list_size:
        is_lst2_exhausted = current_idx_lst2 >= len(lst2)
        is_lst1_exhausted = current_idx_lst1 >= len(lst1)
        first_unmerged_lst1 = lst1[current_idx_lst1]
        first_unmerged_lst2 = lst2[current_idx_lst2]

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

