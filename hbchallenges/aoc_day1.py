def part1(target_num, entries):

    for x in entries:
        for y in entries:
           if x + y == target_num:
               return x, y
            
def part2(target_num, entries):
    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == target_num:
                    return x, y, z

if __name__ == "__main__":
    with open("aoc_day1.txt") as f:
        nums = [int(line) for line in f.readlines()]

    print("Part 1:")
    x, y = part1(2020, nums)
    print(x * y)

    print("Part 2:")
    x, y, z = part2(2020, nums)
    print(x * y * z)