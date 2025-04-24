counter = []
for i in range(289123456, 389123457):
    cnt = 0
    cnt_k = 0
    for k in range(2, (i // 2) + 1):
        if i % k == 0:
            cnt += 1
        if cnt > 3:
            cnt_k = 0
            break
        if cnt == 3:
            cnt_k = k
    if cnt == 3:
        counter.append([i, cnt_k])
for i in counter:
    print(*i, end=' ')
