# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
# 4-27-2022
# Author: theck3

def array_front9(nums):
    length = len(nums)
    end = length
    if end > 4:
        end = 4

    for i in range(end):
        if nums[i] == 9:
            return True
    return False
