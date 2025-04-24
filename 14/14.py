for p in range(1, 27):
    for x in range(0, p):
        for y in range(0, p):
            for z in range(0, p):
                for w in range(0, p):
                    if (x + 1)*p**2 + (3 + z - w) * p - 4 == 0:
                        print(x + z * p + y * p**2)