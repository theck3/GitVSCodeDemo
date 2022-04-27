# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is
# whatever is there. Return a new string which is 3 copies of the front. 
# 4-26-2022
# Author: theck3

def front3(str):
    length = len(str)
    
    if length < 3:
        return str * 3
    else:
        return (str[0:3]) * 3
