"""
https://inf-ege.sdamgia.ru/problem?id=27687
"""
file = open('24_3.txt').readline()
counter = 0
countermax = 0
for i in file:
    if i == 'Y':
        counter += 1
    else:
        countermax = max(countermax, counter)
        counter = 0
print(countermax)