file = open('24_21421.txt').readline()
incorrect = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z']
a = []
b = ''
maxlen = 0
for i in file:
    if i not in incorrect:
        b += i
    else:
        a.append(b)
        b = ''
a = list(set(a))
a.remove('')
for i in a:
    if i[0] == '0':
        i = i[1:]
        try:
            i2 = int(i, 12)
            if i2 % 2 == 0:
                maxlen = max(maxlen, len(i))
        except:
            pass
print(maxlen)
