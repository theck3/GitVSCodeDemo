# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
# Both arrays will be length 1 or more.
# 4-27-2022
# Author: theck3

def common_end(a, b):
    if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    else:
        return False