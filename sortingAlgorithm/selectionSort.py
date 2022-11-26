def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] =  arr[min_index], arr[i]

arr = [8, 5, 4, 10, 9]
selectionSort(arr)
print(arr)