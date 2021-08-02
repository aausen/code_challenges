def print_every_other(given_str):
    even = []
    odd = []
    for idx, char in enumerate(given_str):
        if idx % 2 == 0:
            even.append(char)
        else:
            odd.append(char) 
    new_even = " ".join(even)
    new_odd = " ".join(odd)
    print(new_even + new_odd)

print_every_other("Hacker")