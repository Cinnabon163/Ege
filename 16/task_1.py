# https://education.yandex.ru/ege/task/d60219a0-126c-4892-b4ee-224c06986326

def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * f(n - 2)

print(f(24))
    

