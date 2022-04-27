# Given a string and a non-negative int n, return a larger string that is n copies of the original string. 
# 4-27-2022
# Author: theck3

def string_times(str, n):
    if n < 0:
        return -1
    else:
        return str * n