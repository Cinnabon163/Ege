# https://inf-ege.sdamgia.ru/problem?id=81497
"""
Пусть R — сумма максимального и минимального
 простых делителей целого числа, не считая единицы 
 и самого числа. Если у числа нет простых делителей, 
 то считаем значение R равным нулю. Напишите программу, 
 которая перебирает целые числа, большие 6_000_000, 
 в порядке возрастания и ищет среди них первые шесть 
 таких чисел, для которых R заканчивается на 19.
"""
"""
1. Получать R для числа
1.1. Научиться искать простые делители числа
1.1.1 Научиться генерить простые числа (Решето Эратосфена)
1.1.2 Выбирать из них делители (проверять делится личисло на них)
1.1.3 Знать где максимальный и минимальный
2. По циклу идём пока не соберем 6 чисел, R которых оканч. на 19
"""
# https://ru.wikipedia.org/wiki/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%B0%D1%8F_%D1%82%D0%B5%D0%BE%D1%80%D0%B5%D0%BC%D0%B0_%D0%B0%D1%80%D0%B8%D1%84%D0%BC%D0%B5%D1%82%D0%B8%D0%BA%D0%B8

def RE(n) -> list:
    # решето Эратосфена
    primes_bitmap = [True] * (n+1) # начинаем с 1
    primes_bitmap[0] = False
    primes_bitmap[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes_bitmap[i]:
            for j in range(i*i, n+1, i):
                primes_bitmap[j] = False
    primes = [i for i in range(n+1) if primes_bitmap[i]]
    return primes

def R(n):
    # генерим числа до n с помощью RE(n).
    # проверяем кто из них делитель
    primes_before_n = RE(n)
    dividers = []
    for i in primes_before_n:
        if n % i == 0:
            dividers.append(i)
    min_r = dividers[0]
    max_r = dividers[-1]
    return min_r + max_r

numbers = []
n = 6000001
while len(numbers) < 6:
    R = R(n)
    if R % 100 == 19:
        numbers.append()