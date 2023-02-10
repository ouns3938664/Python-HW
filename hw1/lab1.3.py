maxValue = int(input("Enter Max Value: "))
oeb = input("Enter O/E/B (Odd,Even,Both): ")
yn = input("Y/N(Only prime?): ")


def POE(maxValue, oeb, yn):
    if maxValue < 1:
        return
    if oeb == 'B' and yn == 'N':
        if maxValue > 1:
            for j in range(2, int(maxValue/2) + 1):

                if (maxValue % j) == 0:
                    print(maxValue, "is not a prime number")
                    break
            else:
                print(maxValue, "is a prime number")
        else:
            print(maxValue, "is not a prime number")

    if oeb == 'B' and yn == 'Y':
        if maxValue > 1:
            for j in range(2, int(maxValue/2) + 1):

                if (maxValue % j) == 0:

                    break
            else:
                print(maxValue, "is a prime number")

    if oeb == 'O' and yn == 'N':
        if (maxValue % 2) == 1:
            if maxValue > 1:
                for j in range(2, int(maxValue/2) + 1):

                    if (maxValue % j) == 0:
                        print(maxValue, "is not a prime number")
                        break
                else:
                    print(maxValue, "is a prime number")
            else:
                print(maxValue, "is not a prime number")

    if oeb == 'O' and yn == 'Y':
        if (maxValue % 2) == 1:
            if maxValue > 1:
                for j in range(2, int(maxValue/2) + 1):

                    if (maxValue % j) == 0:
                        break
                else:
                    print(maxValue, "is a prime number")

    if oeb == 'E' and yn == 'N':
        if (maxValue % 2) == 0:
            if maxValue > 1:
                for j in range(2, int(maxValue/2) + 1):

                    if (maxValue % j) == 0:
                        print(maxValue, "is not a prime number")
                        break
                else:
                    print(maxValue, "is a prime number")
            else:
                print(maxValue, "is not a prime number")

    if oeb == 'E' and yn == 'Y':
        if (maxValue % 2) == 0:
            if maxValue > 1:
                for j in range(2, int(maxValue/2) + 1):

                    if (maxValue % j) == 0:
                        break
                else:
                    print(maxValue, "is a prime number")
    maxValue -= 1
    POE(maxValue, oeb, yn)


POE(maxValue, oeb, yn)
