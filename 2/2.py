"""
Ссылка на задание https://inf-ege.sdamgia.ru/problem?id=15097
"""
print('x y z')
for x in (0,1):
    for y in (0,1):
        for z in (0,1):
            if ((x == z) or (x <= (y and z))) == 0:
                print(x,y,z)