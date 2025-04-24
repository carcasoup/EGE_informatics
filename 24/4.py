file = open('zadacha-24-09c68d1d-f81e-450e-827b-aefe8d0ab8de.txt').readline()
a = []
symbols = '-*'
b = ''
for i in range(len(file) - 1):
    b += file[i]
    if file[i] in symbols and file[i + 1] in symbols:
        a.append(b)
        b = ''
for i in range(len(a)):
    a[i] = a[i].split('*')
    for k in range(len(a[i])):
        a[i][k] = a[i][k].split('-')
for i in a:
    print(i)