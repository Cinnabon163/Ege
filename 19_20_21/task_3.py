from functools import lru_cache
import math

@lru_cache(maxsize=None)
def f(a, b, n):
    if a+b >= 128 or n > 3:
        return n == 3
    moves = [
        f(a*2, b, n + 1),
        f(a*2, b*2, n + 1),
        f(a, b*2, n + 1)
        ]
    if n % 2 == 1:
        return all(moves)
    return any(moves)

for i in range(1, 50+1):
    if f(16, i, 0):
        print(i, end=',')