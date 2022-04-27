# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return
# True only if both are negative. 
# 4-26-2022
# Author: theck3

def pos_neg(a, b, negative):
    if negative is True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return True
    else:
        return False 