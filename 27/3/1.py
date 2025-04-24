A = open('27_a-ff2754b8-04f8-4c75-a9d7-19034cdd4191.txt').readlines()[1:]
B = open('27_b-8a18111c-7542-497f-85eb-426fae5cd4b9.txt').readlines()[1:]
clusterA = [[], []]
clusterB = [[], [], []]
for i in A:
    x, y = [float(k) for k in i.replace(',', '.').split()]
    if y > 0:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])
for i in B:
    x, y = [float(k) for k in i.replace(',', '.').split()]
    if x < -5:
        clusterB[0].append([x, y])
    elif y < -4:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])


def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(cluster):
    return sorted(cluster, key=lambda x: sum([d(x, i) for i in cluster]))[0]


answer1 = [center(clusterA[0]), center(clusterA[1])]
answer2 = [center(clusterB[0]), center(clusterB[1]), center(clusterB[2])]

print(int(10000 * (answer1[0][0] + answer1[1][0]) / 2), int(10000 * (answer1[0][1] + answer1[1][1]) / 2))
print(int(10000 * (answer2[0][0] + answer2[1][0] + answer2[2][0]) / 3),
      int(10000 * (answer2[0][1] + answer2[1][1] + answer2[2][1]) / 3))
