def bubbleSort(myArray):
    limit = len(myArray)
    while limit != 0:
        for i in range(limit-1):
            if myArray[i] > myArray[i+1]:
                (myArray[i], myArray[i+1]) = (myArray[i+1], myArray[i])
        limit -= 1


myArray = [11, 4, 7, 5, 10, 9, 13, 1]
bubbleSort(myArray)
print(myArray)
