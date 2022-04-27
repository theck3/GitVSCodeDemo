# Given two int values, return their sum. Unless the two values are the same, then return double their sum. 
# 4-26-2022
# Author: Tyler Heckman

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b