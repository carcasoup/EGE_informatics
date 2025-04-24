"""
https://inf-ege.sdamgia.ru/problem?id=27421
"""
file = open('24_1.txt').readline()
counter = 1
countermax = 0
for i in range(len(file) - 1):
    if file[i] != file[i+1]:
        counter += 1
    else:
        countermax = max(countermax, counter)
        counter = 1
print(countermax)