def f(x, n):
    if x >= 151 or n > 4:
        return n % 2 == 0
    moves = []
    if (x + 1) % 3 != 0:
        moves.append(f(x + 1, n + 1))
    if (x + 2) % 3 != 0:
        moves.append(f(x + 2, n + 1))
    if (x*2) % 3 != 0:
        moves.append(f(x*2, n + 1))

    if n % 2 == 0:
        return all(moves)
    return any(moves)

for i in range(1, 150):
    if i % 3 != 0:
        if f(i, 0):
            print(i, end=',')