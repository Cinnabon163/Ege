for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                F = (z == (not(y))) and ((not(x)) or y) and w
                if F == 1:
                    print(z, x, w, y)

            