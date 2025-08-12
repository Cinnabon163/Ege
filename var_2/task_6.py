from turtle import*
tracer(0)
left(90)
for i in range(6):
    forward(10*25)
    right(60)
pu()
count = 0
for x in range(16):
    for y in range(16):
        goto(x*25, y*25)
        dot(5)
        count += 1
print(count)
done()