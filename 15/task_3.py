def f(x):
    l1 = x % 30 == 0
    l2 = x % 45 == 0
    return (l1 and not(l2))

for x in [30,60,90]:
    print(f(x))
