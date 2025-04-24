"""
https://inf-ege.sdamgia.ru/problem?id=27686
"""
counter = 0
countermax = 0
file = open('24_2.txt').readline()
for line in file:
    if line == 'X':
        counter += 1
    else:
        countermax = max(countermax, counter)
        counter = 0

print(countermax)