# https://education.yandex.ru/ege/task/7f679fe9-e69a-4764-8d0e-61c52af8712b
import sys
import time 
sys.setrecursionlimit(200000)

def f(n):
    global count
    count += 1
    if n <= 1:
        return 1
    if n > 1 and n % 100 == 0:
        return f(n - 1) * f(n - 2) + f(1)
    if n > 1 and n % 100 != 0:
        return n * f(n - 1)

count = 0
start = time.time()
f(2042)
end = time.time()
print(count)
print(start - end) 