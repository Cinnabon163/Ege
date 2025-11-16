#https://inf-ege.sdamgia.ru/problem?id=37337

numbers = []
with open('17.txt') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

count = 0
max_sum = -1
for i, _ in enumerate(numbers[1:], 1):
    if numbers[i-1] % 7 == 0 or numbers[i] % 7 == 0:
        if numbers[i-1] % 160 != numbers[i] % 160:
            count += 1
            if cur_sum := numbers[i-1] + numbers[i] > max_sum:
                max_sum = cur_sum


max_sum = [2123, 3447, 199, 3445, 900, 234]