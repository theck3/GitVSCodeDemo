# Given an array of ints, return the number of 9's in the array. 
# 4-27-2022
# Author: theck3   

def array_count9(nums):
    counter = 0
    target = 9
    for num in nums:
        if num == target:
            counter+=1
        else:
            counter+=0
    return counter
