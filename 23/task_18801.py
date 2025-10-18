# https://inf-ege.sdamgia.ru/problem?id=18801

def F(x, y):
    if x == y: return 1

    if x > y: return 0

    if x < y: return F(x+1, y) + F(x*3, y) + F(x+2, y)

print(F(2, 9)*F(9, 11)*F(11, 12))


print(F(2, 9))
print(F(9, 11))
print(F(11, 12))

