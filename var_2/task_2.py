print('wxyz')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                F = (x and not(y)) or (y == z) or not(w)
                if F == 0:
                    print(w, x, y, z)
                