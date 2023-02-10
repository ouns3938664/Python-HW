def selectionSort(array, size):
    for i in range(size):
        minNum = i
        for j in range(i + 1, size):
            if array[j] < array[minNum]:
                minNum = j
        (array[i], array[minNum]) = (array[minNum], array[i])


arr = [11, 4, 7, 5, 10, 9, 13, 1]
size = len(arr)
selectionSort(arr, size)
print(arr)
