def f(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return f(n -1) + 1
    if n > 0 and n % 2 == 0:
        return f(n//2)
a = 0
for i in range(100000000):
    if f(i) == 4:
        a += 1
        print(a)