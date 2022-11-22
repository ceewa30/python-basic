from array import *

my_array = array('i',[1,2,3,4,5])

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

print(productOfArray(my_array))
