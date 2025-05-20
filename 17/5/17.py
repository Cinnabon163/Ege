numbers = []
with open ("data/17.txt") as f:
    for line in f:
        numbers.append(int(line))

def mod(num):
    return num if num > 0 else -num

positive_count = 0
negative_count = 0

for num in numbers:
    if num >= 0:
        positive_count += 1
    else:
        if num < 0:
            negative_count += 1


result = mod(positive_count - negative_count)
print(result)