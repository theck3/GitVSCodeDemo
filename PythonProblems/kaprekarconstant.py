# Kaprekar's Constant = 6174. The rule is that the number given must have at least 2 unique digits.
# After taking in the input, we check if that rule is met. Then, we put the number in descending
# and ascending order. After subtracting the ascending order number from the descending order number
# we will get a result of 6174.
# 5/7/2022
# Author: theck3

kaprekarsConstant = 6174

def kaprekar(number):
  # turn the number into a list
  numToList = [int(x) for x in str(number)]

  # check if all the numbers are the same
  if numToList.count(numToList[0]) == len(numToList):
    print("Please enter a number with at least 2 unique digits.")
  else:
    # sort list in descending and ascending order
    descendingOrder = sorted(numToList, reverse=True)
    print(descendingOrder)
    ascendingOrder = sorted(numToList)
    print(ascendingOrder)

    # convert descending list to int
    d_num = [str(d_integer) for d_integer in descendingOrder]
    d_string = "".join(d_num)
    d_res = int(d_string)
    print (d_res)

    # convert ascending list to int
    a_num = [str(a_integer) for a_integer in ascendingOrder]
    a_string = "".join(a_num)
    a_res = int(a_string)
    print (a_res)

    # subtract ascending from descending
    res = d_res - a_res
    print(res)

    # if res != kaprekarsConstant, then redo the process
    if res != kaprekarsConstant:
      kaprekar(res)
    else:
      print("success!")


number = input("Enter a 4 digit number that has at least 2 unique digits: ")
kaprekar(number)
