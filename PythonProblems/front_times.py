# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there
# if the string is less than length 3. Return n copies of the front. 
# 4-27-2022
# Author: theck3   

def front_times(str, n):
    length = len(str)
    if length < 3:
        return str * n
    else:
        front_string = str[0:3]
        return front_string * n
        