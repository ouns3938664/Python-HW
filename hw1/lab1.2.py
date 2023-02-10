star = "*"
space = " "
height = int(input("Enter height:"))
count = int(input("Enter number of diamond:"))


def diamond(height, count):
    n = 1
    while (n <= count):
        if height and count > 0:
            for i in range(height):
                print(space * (height-i), star * (i*2+1))
            for i in range(height-2, -1, -1):
                print(space * (height-i), star * (i*2+1))

        else:
            print("error")
            break
        n += 1
    return " "


print(diamond(height, count))
