# the function will take in a list
# create a new list to append to 
# look at each element
# append to the front of the list
def reverse_str(string_list):
    reversed_list = []
    for el in string_list:
        reversed_list.insert(0, el)
    return reversed_list

print(reverse_str(['e', 'i', 'n', 'n', 'a']))