def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        second_num = target - num
        if second_num in seen:
            return [seen[second_num], i]
        else:
            seen[num] = i

def max_sub_array(nums):
    for i in range(1, len(nums)):
        if nums[i -1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

# in this example we start at index 1 so that we can look backwards
# we loop through all the nums
# if the previous num is greater than 0 (being able to increase our sum)
# then we alter our current num to be the sum of num plus the previous
# this will continue through the whole list and in the end 
# we return max of the nums