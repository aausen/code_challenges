def highest_product(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 numbers!')

    
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
   
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        if current * highest_product_of_2 > highest_product_of_3:
            highest_product_of_3 = current * highest_product_of_2

        if current * highest > highest_product_of_2:
            highest_product_of_2 = current * highest

        if current * lowest < lowest_product_of_2:
            lowest_product_of_2 = current * lowest_product_of_2

        if current > highest:
            highest = current

        if current < lowest:
            lowest = current
        
    return highest_product_of_3