for x in range(2300, 0, -1):
    num = 7**350 + 7**150 - x
    num_7 = ''
    while num > 0:
        num_7 += str(num%7)
        num //= 7
    if num_7.count('0') == 200:
        print(x)
        break
"""
Ответ: 2001
"""