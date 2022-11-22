def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
arr = [19, 13, 6, 2, 18, 8]
bubbleSort(arr)
print(arr)