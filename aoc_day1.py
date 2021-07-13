def find_num_sum():

    nums = open("aoc_day1.txt")

    for i, num in enumerate(nums):
        
        if num[i] + num[i + 1] == 2020:
            return num[i]*num[i + 1]
        