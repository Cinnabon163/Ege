# https://inf-ege.sdamgia.ru/problem?id=81491


def RE(n) -> list:
    primes_bitmap = [True] * (n+1)
    primes_bitmap[0] = False
    primes_bitmap[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes_bitmap[i]:
            for j in range(i*i, n+1, i):
                primes_bitmap[j] = False
    primes = [i for i in range(n+1) if primes_bitmap[i]]
    return primes


def R(n):
    primes_before_n = RE(n)
    dividers = []
    for i in primes_before_n:
        if n % i == 0:
            dividers.append(i)
    min_r = dividers[0]
    max_r = dividers[-1]
    return min_r + max_r


numbers = []
n = 7000001

while len(numbers) < 5:
    M = R(n)
    if M % 100 == 13:
        numbers.append((n, M))
    n += 1

for num, R in numbers:
    print(num, R)
