#19
def f(x, y):
    if x <= 25:
        return y % 2 == 0
    if y == 0:
        return 0
    h = [f(x - 2, y - 1), f(x - 5, y - 1), f(x // 3, y - 1)]
    return any(h) if y % 2 else all(h)

print([s for s in range(26, 300) if not f(s, 2) and f(s, 4)])