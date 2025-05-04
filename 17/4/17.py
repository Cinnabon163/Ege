numbers = []
with open ("data/17.txt", "r") as f:
    for line in f:
        numbers.append(int(line))

def mod(num):
    return num if num > 0 else -num

positives = 0
negatives = 0

for num in numbers:
    if num >= 0:
        positives += num
    if num < 0:
        negatives += -num

result = mod(positives - negatives)

print(result)
    
