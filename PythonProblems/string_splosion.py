# Given a non-empty string like "Code" return a string like "CCoCodCode". 
# 4-27-2022
# Author: theck3   

def string_splosion(str):
    result = ''

    # for each char in the range of 0 to length of string, new string = new string + passed string up until chars+1

    for chars in range(len(str)):
        result = result + str[:chars+1]

    return result