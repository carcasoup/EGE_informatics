file = open('17_21416.txt').readlines()
counter = 0
maxsum = 0
print(len(file))
a = sum([int(i) for i in file if int(i) < 0])
for i in range(len(file) - 2):
    line = sorted([int(i) for i in file[i:i+3]])
    if line[0] * line[2] > a:
        counter += 1
        maxsum = max(maxsum, sum(line))
print(counter)
print(maxsum)


