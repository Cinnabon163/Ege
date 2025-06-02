from functools import lru_cache

@lru_cache(maxsize=None)
def f(a, n):
    if a >= 61:
        return n == 1
    moves = [
        f(a + 3, n + 1),
        f(a*2, n + 1)
        ]
    if n % 2 == 0:
        return any(moves)
    return all(moves)

for i in range(1, 60+1):
    if f(i, 0):
        print(i, end=',')