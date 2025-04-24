file = open('27_A.txt').readlines()[1:]
cluster1 = []
cluster2 = []


file2 = open('27_B.txt').readlines()[1:]
clusterB1 = []
clusterB2 = []
clusterB3 = []

for i in file2:
    i2 = i.replace(',', '.')
    x, y = float(i2.split()[0]), float(i2.split()[1])
    if y < 3:
        clusterB1.append([x, y])
    elif y < 7:
        clusterB2.append([x, y])
    else:
        clusterB3.append([x, y])


for i in file:
    i2 = i.replace(',', '.')
    x, y = float(i2.split()[0]), float(i2.split()[1])
    if y < 3:
        cluster1.append([x, y])
    else:
        cluster2.append([x, y])


def d(a, b):
    x, y = a
    x1, y1 = b
    return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

def center(cluster):
    a = []
    for i in cluster:
        summ = sum(d(i, k) for k in cluster)
        a.append([summ, i])
    return min(a)[1]

Px = (center(cluster1)[0] + center(cluster2)[0]) * 5000
Py = (center(cluster1)[1] + center(cluster2)[1]) * 5000
print(Px, Py)

Pbx = (center(clusterB1)[0] + center(clusterB2)[0] + center(clusterB3)[0]) * 10000 / 3
Pby = (center(clusterB1)[1] + center(clusterB2)[1] + center(clusterB3)[1]) * 10000 / 3
print(Pbx, Pby)


