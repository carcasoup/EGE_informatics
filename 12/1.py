for i in range(3, 10001):
    a = '3' + '1' * i
    while '31' in a or '211' in a or '1111' in a:
        if '31' in a:
            a = a.replace('31', '1', 1)
        if '211' in a:
            a = a.replace('211', '13', 1)
        if '1111' in a:
            a = a.replace('1111', '2', 1)
    if sum([int(i) for i in a]) == 15:
        print(i)
        break