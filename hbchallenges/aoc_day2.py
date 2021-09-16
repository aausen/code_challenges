# how many passwords are valid according to their policies

# start a counter
# read the file line by line
# parse through text to find rule and password split on :
# if the password matches the rule, add to the count
# if 

def part1(entries):
    counter = 0

    for line in entries:
        lst = line.split(":")
        rule = lst[0]
        password = lst [-1]
        


if __name__ == "__main__":
    with open("aoc_day2.txt") as f:
        rules = [line for line in f.readlines()]

    print("Part 1:")    
    part1(rules)