# Given a string, return a new string where the first and last chars have been exchanged (code -> eodc)
# 4-26-2022
# Author: theck3

def front_back(str):
    length = len(str)
    first = str[0]
    last = str[length-1]
    new_string = last + str[1:length-1] + first
    return new_string