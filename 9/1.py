file = open('zadacha-09-e98eedaf-a8b8-495e-93f5-34835d16376d.txt', 'r')
counter1 = 0
for i in file:
    i2 = [int(k) for k in i.split()]
    if sum(i2) % 2 == 1:
        for j in range(len(i2)):
            if i2.count(i2[j]) == 1:
                if j == 0:
                    if i2[j] % i2[j + 1] == 0:
                        counter1 += 1

                elif j == 5:
                    if i2[j] % i2[j - 1] == 0:
                        counter1 += 1

                else:
                    if i2[j] % (i2[j + 1] + i2[j - 1]) == 0:
                        counter1 += 1
print(counter1)
