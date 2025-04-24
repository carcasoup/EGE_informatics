"""
Ссылка на задание: https://education.yandex.ru/ege/task/67a6ffab-6297-4a25-a7cd-e2c0c9f85bb7
"""
print('x y w ')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if ((x <= y) and (z or (not z))) == 0:
                print(x, y, z)

