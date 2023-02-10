star = "*"
space = " "
countStar = 1
countSpace = 4
while countStar <= 9:
    print((space*countSpace)+(star*countStar)+(space*countSpace))
    countStar += 2
    countSpace -= 1

countStar -= 2
countSpace += 1


while countStar >= 1:
    countStar -= 2
    countSpace += 1
    print((space*countSpace)+(star*countStar)+(space*countSpace))
