# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# 4-27-2022
# Author: theck3

def string_bits(str):
    result = ''
    length = len(str)

    for i in range(length):
        if i % 2 == 0:
            result = result + str[i]
    return result        
