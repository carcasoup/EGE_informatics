file = open('17_21903.txt').readlines()
mini = min([int(i) for i in file if len(str(abs(int(i)))) == 3 and abs(int(i)) % 100 == 15])
counter = 0
mini2 = 999999
for i in range(len(file) - 2):
    threes = [int(file[i]), int(file[i + 1]), int(file[i + 2])]
    if (min(threes) >= 0 or max(threes) <= 0) and min(threes) * max(threes) > mini ** 2:
        counter += 1
        mini2 = min(mini2, min(threes) * max(threes))
print(counter)
print(mini2)

"""
Ответ: 3507 0 
"""