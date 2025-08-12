def f(x, A):
    return (x > 78) or (A > x)

for A in range(100):
    done = True
    for x in range(1, 79):
        if not f(x, A):
            done = False
    if done:
        print(A)