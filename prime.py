def numbers(n:int):
    for i in range(0,n):
        if i%2 == 0:
            print(i)

def is_odd(n:int) -> bool:
    return n%2 != 0

# является ли число простым
# 7 -> True
# 12 -> False
# n делится ТОЛЬКО на себя и на 1
# n НЕ делится ни на одно из чисел 2...n-1
def is_prime(n:int) -> bool:
    if n < 2:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True


# вывести список всех простых чисел до K
def primes(K) -> list:
    primes_numbers = []
    for num in range(2, K):
        prime_number = True
        for i in range(2, num):
            if num % i == 0:
                prime_number = False
        if prime_number:
            primes_numbers.append(num)
    return primes_numbers

print(primes(11))

# напиши ещё тесты для разных чисел
# assert primes(11) == [2, 3, 5, 7, 11]