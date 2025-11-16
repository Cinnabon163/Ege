# https://inf-ege.sdamgia.ru/problem?id=37336

numbers = []
with open('17.txt') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

count = 0
max_sum = -10001
for i, _ in enumerate(numbers[1:], 1):
    if numbers[i-1] % 3 == 0 or numbers[i] % 3 == 0:
        count += 1
        pair_sum = numbers[i-1] + numbers[i]
        if max_sum < pair_sum:
            max_sum = pair_sum

print(count, max_sum)
