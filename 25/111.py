a = []
for i in range(1125000, 9999999):
    for k in range(17, (i // 2) + 1, 10):
        if i % k == 0:
            a.append((i, k))
            break
    if len(a) == 5:
        break
for i in a:
    print(*i)