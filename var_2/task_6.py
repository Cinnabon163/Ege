from turtle import*
tracer(0)
left(90)
for i in range(6):
    forward(10*25)
    right(60)
pu()
count = 0
<<<<<<< HEAD
for x in range(21):
    for y in range(21):
        goto(x * 25, y * 25 - 125)
        dot(3)
        count += 1
=======


for x in range(21):
    for y in range(21):
        goto(x * 25, y * 25 - 125)
        dot(2)
>>>>>>> 3095b5bcd5f3e1508f8fcbf8946afd8f691a4f07
print(count)
done()
