numbers = []
with open ("data/17.txt") as f:
    for line in f:
        numbers.append(int(line))

def mod(num):
    return num if num > 0 else -num

max_positive = -10000
min_negative = 10000

for num in numbers:
    if num >= 0:
        if num > max_positive:
            max_positive = num
    if num < 0:
        if num < min_negative:
            min_negative = num

result = max_positive - min_negative

print(result)