# https://inf-ege.sdamgia.ru/problem?id=81492 


cargo = ''
count = 0
with open('26.txt') as f:
    n, m = map(int, f.readline().strip().split(' '))
    cargo = [int(l.strip()) for l in f.readlines()]
    cargo.sort(reverse=True)

res = []

while len(cargo):
    count += 1
    box = []
    w = 0
    for c in cargo[:]:
        if w + c <= m:
            w += c
            box.append(c)
            print(count, box)
            cargo.remove(c)
    res.append(box)

print(n, m)
print(res[-2])
print(count, sum(res[-2]))











