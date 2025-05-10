"""
Задание  C3D450 с bank-ege.ru
"""
file = open('Задание_26_C3D450.txt')
n = int(file.readline())
file = file.readlines()
for i in range(len(file)):
    file[i] = [int(k) for k in file[i].split()]
file.sort(key=lambda x: x[0])
ryad_number = 0
min_pair = 100001
unique_ryad = file[:][0]
for i in file:
    if unique_ryad.count(i[0]) >= 4:
        if [i[0], i[1] + 1] in file:
            if [i[0], i[1] + 2] in file and [i[0], i[1] - 1] in file:
                if i[1] < min_pair:
                    min_pair = i[1]
                    ryad_number = i[0]

print(min_pair, ryad_number)
