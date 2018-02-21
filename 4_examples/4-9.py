apart = [[101, 102, 103, 104],
         [201, 202, 203, 204],
         [301, 302, 303, 304],
         [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for a in apart:
    for number in a:
        if number not in arrears:
            print('Deliver to ', number)