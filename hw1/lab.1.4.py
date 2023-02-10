def harmonic(n):

    if n < 2:
        print('limit of 1 = 1')
        return 1
    else:
        x = 1/n+(harmonic(n-1))
        print('limit of '+str(n)+' = '+str(x))
        return x


n = int(input('Enter Value: '))
harmonic(n)
