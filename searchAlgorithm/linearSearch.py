def linearSearch(arr, value):
    for i in range(len(arr)):
        if (arr[i] == value):
            return i
    return -1

print(linearSearch([20,10,30,40,60], 30))