from turtle import *
tracer(0)
k = 40
rt(90)
pu()
fd(10*k)
pd()
rt(180)
rt(315)
for _ in range(7):
    fd(16*k)
    rt(45)
    fd(8*k)
    rt(135)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(4, 'red')
done()