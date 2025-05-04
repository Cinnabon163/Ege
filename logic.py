
def eq(x, y):
    return not x and not y or x and y

def implic(x, y):
    return not x or y

def F(a, b, c, d):
    return int(implic(a, b) and implic(b, not c) and eq(c, not d))

for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            for d in [0, 1]:
                print(a, b, c, d, "|", F(a, b, c, d))


