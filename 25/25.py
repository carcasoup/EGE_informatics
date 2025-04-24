from fnmatch import fnmatch
for i in range(10**8):
    if fnmatch(str(i), '2*4257?4') and i % 272 == 0 and sum([int(k) for k in str(i)]) % 9 == 0:
        print(i, i // 272)