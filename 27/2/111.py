clustersA = open('27_A_21425.txt').readlines()
clustersB = open('27_B_21425.txt').readlines()
A = [[], []]
B = [[], [], []]
for i in clustersA:
    x, y = [float(k) for k in i.replace(',', '.').split()]
    if y > 0:
        A[0].append([x, y])
    else:
        A[1].append([x, y])
for i in clustersB:
    x, y = [float(k) for k in i.replace(',', '.').split()]
    if x < 0:
        B[0].append([x, y])
    elif y > 0:
        B[1].append([x, y])
    else:
        B[2].append([x, y])


def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(cluster):
    return sorted(cluster, key=lambda x: sum([d(i, x) for i in cluster]))[0]


answer1 = [center(A[0]), center(A[1])]
answer2 = [center(B[0]), center(B[1]), center(B[2])]

print(int(10000 * (answer1[0][0] + answer1[1][0]) / 2), int(10000 * (answer1[0][1] + answer1[1][1]) / 2))
print(int(10000 * (answer2[0][0] + answer2[1][0] + answer2[2][0]) / 3),
      int(10000 * (answer2[0][1] + answer2[1][1] + answer2[2][1]) / 3))
