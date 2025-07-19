from functools import lru_cache

THR = 41

@lru_cache(maxsize=None)
def f(a, n):
    if a >= THR or n > 1:
        return n == 1
    moves = [
        f(a + 1, n + 1),
        f(a + 2, n + 1),
        f(a*2, n + 1)
        ]
    if n % 2 == 0:
        return any(moves)
    
    return any(moves)

for i in range(1, THR+1):
    if f(i, 0):
        print(i, end=',')
