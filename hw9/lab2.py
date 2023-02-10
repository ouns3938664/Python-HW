def binarySearch(data, fIndex, lIndex, ip):

    if lIndex >= fIndex:
        med = (lIndex + fIndex) // 2
        if data[med] == ip:
            return med
        elif data[med] < ip:
            fIndex = med + 1
            return binarySearch(data, fIndex, lIndex, ip)
        else:
            lIndex = med - 1
            return binarySearch(data, lIndex, fIndex, ip)
    else:
        print('Hmmm Its doesnt seem here.')
        return


data = [7, 10, 12, 14, 16, 20, 29, 37]


ans1 = binarySearch(data, 0, 7, 14)
ans2 = binarySearch(data, 0, 7, 29)


if ans1 != None:
    print('Oh! num 14 its there at Index : '+str(ans1))
if ans2 != None:
    print('Oh! num 29 its there at Index : '+str(ans2))
