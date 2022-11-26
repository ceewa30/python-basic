import math

def binarySearch(arr, value):
    start = 0
    end = len(arr)-1
    middle = math.floor((start+end)/2)
    while not(arr[middle]==value) and start<=end:
        if value < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if arr[middle] == value:
        return middle
    else:
        return -1


custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))


