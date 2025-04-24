"""
https://inf-ege.sdamgia.ru/problem?id=5497
"""
def F(x, y):
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y) + F(x + 5, y)
    if x > y:
        return 0

print(F(2, 16))