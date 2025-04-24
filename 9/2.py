file = open('9_21408.txt').readlines()
counter = 0
a = []
for i in file:
    line = [int(k) for k in i.split()]
    cnt = []
    cnt1 = []
    for j in line:
        if line.count(j) == 3:
            cnt.append(j)
        if line.count(j) == 1:
            cnt1.append(j)
    if len(cnt) == 6 and len(cnt1) == 1 and max(cnt) > cnt1[0]:
        counter += 1
        a = line
print(counter)
print(a)