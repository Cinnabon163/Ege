# https://inf-ege.sdamgia.ru/problem?id=29672

lines = []
with open("data/24.txt") as f:
    lines = [line.strip() for line in f.readlines()]


count = 0

for l in lines:
    if l.count("E") > l.count("A"):
        count += 1

print(count)



