from array import *


def insertSort(arr):
    for index in range(1, len(arr)):
        currentValue = arr[index]
        currentPosition = index
        print(currentValue)
        while (currentPosition > 0 and arr[currentPosition - 1] > currentValue ):
            arr[currentPosition] = arr[currentPosition - 1]
            currentPosition = currentPosition - 1  
        
        
        arr[currentPosition] = currentValue
        #     # print(arr[j+1])


my_array = [22, 4, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
insertSort(my_array)
print("sorted array: " + str(my_array))

# print(insertSort(my_array))
