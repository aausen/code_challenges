def find_num_sum():

    nums = open("aoc_day1.txt")
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums(i + 1)):
            if num + num2 == 2020:
                return num*num2
            