# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
# 4-27-2022
# Author: theck3

def same_first_last(nums):
    length = len(nums)-1
    first = nums[0]
    last = nums[length]

    if length >= 1 and first == last:
        return True
    else:
        return False
