# Condition: We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble. 
# 4-26-2022
# Author: Tyler Heckman

def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False