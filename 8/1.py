from itertools import product
counter = 0
for i in product('АБВГДЕЖЗИК', repeat=7):
    counter += 1
    if i[0] == 'Ж' and i[-1] == 'К' and len(i) == len(set(i)):
        print(counter, i)
        break