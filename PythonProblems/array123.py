# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
# 4-27-2022
# Author: theck3   

def array123(nums):
    length = len(nums)
    
    for i in range(length-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
    