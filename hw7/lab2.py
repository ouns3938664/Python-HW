def insertionSort(arr):
    l = len(arr)
    for i in range(1, l):
        j = i
        while arr[j] < arr[j-1] and j != 0:
            (myArray[j], myArray[j-1]) = (myArray[j-1], myArray[j])
            j -= 1


myArray = [11, 4, 7, 5, 10, 9, 13, 1]
insertionSort(myArray)
print(myArray)
