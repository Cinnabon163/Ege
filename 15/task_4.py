def f(x, y, A):
    return (x >= 8) or (A < (x*y)) or (y<=7)

for A in range(100):
    done = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not f(x, y, A):
                done = False
    if done:
        print(A)