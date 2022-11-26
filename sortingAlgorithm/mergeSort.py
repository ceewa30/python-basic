
def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]   # arr[0:len(arr)/2]
        rightArr = arr[len(arr)//2:]  # arr[len(arr)/2 : len(arr)]


        # recursion
        mergeSort(leftArr)
        mergeSort(rightArr)

        # merge
        i=0
        j=0
        k=0
        while i < len(leftArr) and j< len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

arr_test = [2, 3, 5, 1, 7, 4, 2, 6, 0]
mergeSort(arr_test)
print(arr_test)

