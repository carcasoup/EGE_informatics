from math import dist


def center(cluster):
    return min(cluster, key=lambda a: sum([dist(a, i) for i in cluster]))


def midfile(clusters):
    coords = [center(i) for i in clusters]
    x, y = sum(j[0] for j in coords) / len(coords), sum(j[1] for j in coords) / len(coords)
    return int(abs(10000 * x)), int(abs(10000 * y))


fileA = open('27_A_21911.txt').readlines()[1:]
fileB = open('27_B_21911.txt').readlines()[1:]
clusterA = [[], []]
clusterB = [[], [], []]
for i in fileA:
    x, y = [float(k) for k in i.replace(',', '.').split()]
    if y > 2:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])
for i in fileB:
    x, y = [float(k) for k in i.replace(',', '.').split()]
    if x < 10:
        clusterB[0].append([x, y])
    elif y > 8:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

print(*midfile(clusterA))
print(*midfile(clusterB))