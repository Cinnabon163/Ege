# https://inf-ege.sdamgia.ru/problem?id=27775

def f(x, y, n):
    if x + y <= 20 or n > 3:
        return n == 3
    moves = [
        f(x - 1, y, n + 1),
        f(x, y - 1, n + 1),
        f(x // 2 + x % 2, y, n + 1),
        f(x, y // 2 + y % 2, n + 1)
    ]
    
    if n % 2 == 0:
        return any(moves) 
    # независимо от того, как будет ходить Ваня.
    return all(moves) # Петя может выиграть своим вторым ходом 

for i in range (100, 10, -1):
    if f(10, i, 0):
        print(i, end=',')