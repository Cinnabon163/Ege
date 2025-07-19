def f(x, A):
    ...

for A in range(100):
    done = True
    for x in range(100):
        if not f(x, A):
            done = False
    if done:
        print(A)