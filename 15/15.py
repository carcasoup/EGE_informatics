for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((5 < y) or (x > 32) or (x + 2 * y < A)):
                flag = False
                break
    if flag:
        print(A)
        break