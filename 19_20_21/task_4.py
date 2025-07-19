from functools import lru_cache
import math

@lru_cache(maxsize=None)
def f(a, b, n):
    if a+b >= 50 or n > 3:
        return n == 3
    moves = [
        f(a+3, b, n + 1),
        f(a*3, b, n + 1),
        f(a, b+3, n + 1),
        f(a, b*3, n + 1)
        ]
    if n % 2 == 1:
        return all(moves)
    return any(moves)

for i in range(2, 45+1):
    if f(4, i, 0):
        print(i, end=',')