def f(x, y, n):
    if x**2 + y**2 >= 14**2 or n > 4:
        return n == 4
    moves = [
        f(2*x, y, n +1),
        f(x, y+3, n +1),
        f(x, y+4, n +1)
    ]
    if n % 2 == 0:
        return all(moves)
    return any(moves)

for i in range(1, 13+1):
    if f(3, i, 0):
        print(i, end=',')

