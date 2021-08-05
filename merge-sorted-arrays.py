def merge_lists(lst1, lst2):
    # take in two lists
    # look at each element to decide which is less
    # add the less one to the list
    # look for next less number
    # if one list runs out, append the rest of remaining list
    merged_list = []
    i = 0 
    j = 0

    for i in lst1:
        for j in lst2:
            if i < j:
                merged_list.append(i)
                i += 1
            if j < i:
                merged_list.append(j)
                j += 1
            
