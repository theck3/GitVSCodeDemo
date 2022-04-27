numberList = [4, 30, 9, 20, 12, 3, 4, 63, 24, 81, 43, 23, 36, 14, 13, 98, 2]
numberList.sort()

print(numberList)
print("Length of list: " + str(len(numberList)))

target = 98
listLength = len(numberList)
current = numberList[listLength//2]

print("Current value being looked at: " + str(current))

def binarySearch(l, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(l)-1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if midpoint == target:
        return target
    elif midpoint < target:
        binarySearch(l, target, low, midpoint-1)
    else:
        binarySearch(l, target, midpoint+1, high)


print(binarySearch(numberList, target))