counter = 0
i = 500001
while counter != 5:
    summi = 0
    for k in range(1, i + 1):
        if i % k == 0:
            summi += k
    if summi % 10 == 6:
        print(i, summi)
        counter += 1
    i += 1