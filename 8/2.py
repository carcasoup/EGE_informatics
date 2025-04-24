from itertools import product
counter = 0
for i in product('ДГИАШЭ', repeat=5):
    if i[0] not in 'ИАЭ' and i[4]  not in 'ДГШ':
        counter += 1
print(counter)