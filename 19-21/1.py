"""
19
def f(x, y):
    if x >= 67:
        return y % 2 == 0
    if y == 0:
        return 0
    h = [f(x + 1, y -1), f(x + 4, y - 1), f(x * 3, y - 1)]
    return any(h) if y % 2 else all(h)

print([i for i in range(1, 67) if not f(i, 1) and f(i, 2)])
"""
def f(x, y):
    if x >= 67:
        return y % 2 == 0
    if y == 0:
        return 0
    h = [f(x + 1, y -1), f(x + 4, y - 1), f(x * 3, y - 1)]
    return any(h) if y % 2 else all(h)

print([i for i in range(1, 67) if not f(i, 3) and f(i, 5)])





