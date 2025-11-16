from turtle import *
lt(90)
k = 50
tracer(0)
down()
for i in range(6):
    rt(36)
    fd(10)
    rt(36)
up()
for x in range(-10,25):
    for y in range(-10,25):
        setpos(x*k,y*k)
        dot(3)
done()