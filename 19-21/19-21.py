#19
"""
def f(x, y):
    if x <= 87:
        return y % 2 == 0
    if y == 0:
        return 0
    h = [f(x - 2, y - 1), f(x // 2, y - 1)]
    return any(h) if y % 2 else all(h)

print(min([s for s in range(89, 300) if f(s, 2)]))
Ответ: 176
"""
#20
"""
def f(x, y):
    if x <= 87:
        return y % 2 == 0
    if y == 0:
        return 0
    h = [f(x - 2, y - 1), f(x // 2, y - 1)]
    return any(h) if y % 2 else all(h)

print([s for s in range(89, 300) if not f(s, 1) and f(s, 3)])
Ответ: 178 179
"""
def f(x, y):
    if x <= 87:
        return y % 2 == 0
    if y == 0:
        return 0
    h = [f(x - 2, y - 1), f(x // 2, y - 1)]
    return any(h) if y % 2 else all(h)

print([s for s in range(89, 300) if not f(s, 2) and f(s, 4)])
