for i in range(5):
    for j in range(5):
        if 4 - j - i > 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')