"""
https://inf-ege.sdamgia.ru/problem?id=68524в
"""
def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return f(x+1, y) + f(x + 2, y) + f(x * 2, y)
    elif x > y:
        return 0

print(f(4, 11) * f(11, 13) * f(13, 15))