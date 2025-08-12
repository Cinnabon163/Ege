def f(x):
    l1 = x % 30 == 0
    l2 = 15 % x == 0 
    return (l1 or l2)

for x in range(2, 100):
    if f(x):
        print(x, end=',')
        



        
