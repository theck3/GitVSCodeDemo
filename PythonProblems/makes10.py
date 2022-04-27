# Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10. 
# 4-26-2022
# Author: Tyler Heckman

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif (a + b) == 10:
        return True
    else:
        return False