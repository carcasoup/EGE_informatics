from itertools import product
counter = 0
for i in product('01234', repeat=6):
    if i[0] not in '01' and i[-1] not in '34':
        counter += 1
print(counter)