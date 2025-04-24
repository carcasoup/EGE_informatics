from turtle import *

tracer(0)
k = 30
lt(90)
for _ in range(6):
    fd(8*k)
    rt(120)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(2, 'red')

done()
