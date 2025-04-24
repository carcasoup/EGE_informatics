for N in range(1, 10000):
    a = bin(N)[2:]
    if a.count('1') % 2 == 0:
        a += '0'
        a = '10' + a[2:]
    else:
        a += '1'
        a = '11' + a[2:]
    r = int(a, 2)
    if r > 480:
        print(N)
        break