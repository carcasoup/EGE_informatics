"""
https://inf-ege.sdamgia.ru/problem?id=17370
"""
a = []
for n in range(100, 3001):
    n1 = bin(n)[3:]
    n2 = int(n1, 2)
    a.append(n2 - n)
print(len(set(a)))