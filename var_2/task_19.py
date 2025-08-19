# https://inf-ege.sdamgia.ru/problem?id=27774

def f(x, y, n):
    if x + y <= 20 or n > 2:
        return n == 2
    moves = [
        f(x - 1, y, n + 1),
        f(x, y - 1, n + 1),
        f(x // 2 + x % 2, y, n + 1),
        f(x, y // 2 + y % 2, n + 1)
    ]
    
    if n % 2 == 1: # ходы Пети - нечётные
        return any(moves) # При ЛЮБОМ ходе Пети
    return any(moves) # выигрываем всегда

for i in range (100, 10, -1):
    if f(10, i, 0):
        print(i, end=',')