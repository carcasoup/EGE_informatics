from re import findall
file = open('24_21908.txt').readline()
a = findall(r'(?:[1-D][0-D]*)*', file)
print(len(max(a, key=len)))
