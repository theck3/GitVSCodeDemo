# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
# 4-27-2022
# Author: theck3

def first_last6(nums):
    length = len(nums)
    first = nums[0]
    last = nums[length-1]

    if first == 6 or last == 6:
        return True
    else:
        return False