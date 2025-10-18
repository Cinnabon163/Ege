# https://inf-ege.sdamgia.ru/problem?id=33528

f = open("26.txt")
N, M = map(int, f.readline().strip().split(' '))
A = []
B = []
for line in f.readlines():
    price, count, kind  = line.strip().split(' ')
    price = int(price)
    count = int(count)
    if kind == 'A':
        A.append((price, count))
    else:
        B.append((price, count))
A.sort()

money = M
for price, count in A:
    if money < price:
        break
    can_buy = min(count, money // price)
    money -= can_buy *  price

B.sort()

bought_B = 0
for price, count in B:
    if money < price:
        break
    can_buy = min(count, money // price)
    bought_B += can_buy
    money -= can_buy * price
print(bought_B, money)
