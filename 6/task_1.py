from turtle import *
screensize(2500,2500)
left(90)
k = 50
tracer(0)
down()
for i in range(7):
    forward(k*10)
    right(120)
up()
for x in range(-10,25):
    for y in range(-10,25):
        setpos(x*k,y*k)
        dot(5)
done()
        
            
