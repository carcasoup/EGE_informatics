from turtle import *
tracer(0)
lt(90)
k = 30
rt(30)
for _ in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(4, 'red')
done()