def f(x, y, A):
    return ((y + x)**2 > 1048) or ((x + 20 < A) and (40 - y < A))

for A in range(100):
    done = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not f(x, y, A):
                done = False
    if done:
        print(A)       

