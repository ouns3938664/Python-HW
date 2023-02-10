def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    leftArr = mergeSort(arr[:len(arr)//2])
    rightArr = mergeSort(arr[len(arr)//2:])
    return merge(leftArr, rightArr)


def merge(leftArr, rightArr):
    mergeArr = []
    leftPointer = rightPointer = 0
    while leftPointer < len(leftArr) and rightPointer < len(rightArr):
        if leftArr[leftPointer] < rightArr[rightPointer]:
            mergeArr.append(leftArr[leftPointer])
            leftPointer += 1
        else:
            mergeArr.append(rightArr[rightPointer])
            rightPointer += 1
    mergeArr.extend(leftArr[leftPointer:])
    mergeArr.extend(rightArr[rightPointer:])
    return mergeArr


mergeArr = mergeSort([29, 10, 14, 37, 14, 20, 7, 16, 12])
print(mergeArr)
