from typing import ForwardRef


def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2: 
        raise IndexError("Getting the product of other numbers at indecies requires at least 2 numbers")
    products_of_all_ints_except_at_index = [None] * len(int_list)
    
    product_so_far = 1

    for i in range(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    product_so_far = 1
    for i in (len(int_list) -1, -1, -1):
        products_of_all_ints_except_at_index[i] *=  product_so_far

    return products_of_all_ints_except_at_index