# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not",
# return the string unchanged. 
# 4-26-2022
# Author: theck3

def not_string(s):
    index = s.find("not")
    if index == 0:
        return s
    else:
        return "not " + s
