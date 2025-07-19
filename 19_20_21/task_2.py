from functools import lru_cache

@lru_cache(maxsize=None)
def f(a, n):
    if a >= 229 or n > 2:
        return n == 2
    
    moves = (
        f(a + 2, n + 1),
        f(a + 3, n + 1),
        f(a + 4, n + 1),
        f(a * 2, n + 1)
    )

    if n % 2 == 0:
        return all(moves)
    else:
        return any(moves)
    
for s in range(1, 229):
    if f(s, 0):
        print(s)
        break