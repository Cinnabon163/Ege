from turtle import *
screensize(1500,1500)
lt(90)
k = 50
tracer(0)
down()
for i in range(6):
    forward(10*k)
    right(60)
up()
for x in range(-10,25):
    for y in range(-10,25):
        setpos(x*k,y*k)
        dot(5)
done()

