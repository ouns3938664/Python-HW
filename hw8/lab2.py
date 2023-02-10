def quickLomuto(arr, front, back):
    if (front >= back):
        return

    pv = arr[back]
    j = front

    for i in range(front, back):
        if (arr[i] <= pv):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[back], arr[j] = arr[j], arr[back]

    quickLomuto(arr, front, j-1)
    quickLomuto(arr, j+1, back)

    return arr


def quickHoarse(arr, front, back):

    if (front >= back):
        return

    pv = arr[back]
    i = front
    j = back

    while (i < j):
        while (arr[i] < pv):
            i += 1

        while (arr[j] > pv):
            j -= 1

        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    quickHoarse(arr, front, i-1)
    quickHoarse(arr, i, back)

    return arr


quickArr0 = quickLomuto([29, 10, 14, 37, 14, 20, 7, 16, 12], 0, 8)
quickArr1 = quickHoarse([29, 10, 14, 37, 14, 20, 7, 16, 12], 0, 8)
print(quickArr0)
print(quickArr1)
