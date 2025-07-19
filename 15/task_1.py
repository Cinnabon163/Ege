def f(x, A):
    l1 = x % 12 == 0
    l2 = x % 5 == 0
    l3 = x % A == 0
    return (l1 and l2) <= l3

for A in range(1, 10):
    done = True
    for x in range(10):
        if not f(x, A):
            done = False
    if done:
        print(A)