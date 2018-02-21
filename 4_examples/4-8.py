for i in range(5):
    for j in range(9 - i):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print('')