from turtle import *
screensize(2500,2500)
left(90)
k = 50
tracer(0)
down()
for _ in range(2):
    forward(k*10)
    right(90)
    forward(k*18)
    right(90)
up()
forward(k*5)
right(90)
forward(k*7)
left(90)
down()
for _ in range(2):
    forward(10*k)
    right(90)
    forward(7*k)
    right(90)
up()
for x in range(-10,25):
    for y in range(-10,25):
        setpos(x*k,y*k)
        dot(5)
done()
        