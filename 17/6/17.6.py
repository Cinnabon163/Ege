import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
data_path = os.path.join(script_dir, "data", "17.txt")

content = []
with open("data/17.6.txt") as f:
    content = f.readlines()

# найти максимальный элемент в последовательности, кратный 36
multiples_of_36 = []
for str_num in content:
    num = int(str_num)
    if num % 36 == 0:
        multiples_of_36.append(num)

max36 = max(multiples_of_36)

def is_positive(x):
    x = int(x)
    return x > 0

def endswith_36(x):
    return str(x)[-2:] == "36"

# не менее чем для двух элементов выполняется хотя бы одно
# из условий (или оба): элемент положительный, заканчивается на 36.
# Сумма элементов тройки не должна быть больше 
# максимального элемента последовательности, кратного 36.
def get_triple_status(current, prev, prev_prev, max36):
    count = 0
    total = 0
    for x in (prev_prev, prev, current):
        if is_positive(x) or endswith_36(x):
            count += 1
        total += int(x)
    return (count > 2 and total < max36, total)



count = 0
totals = []
for i, _ in enumerate(content[2:], 2):
    status = get_triple_status(content[i], content[i-1], content[i-2], max36)
    is_triple_valid = status[0]
    totals.append(status[1])
    if is_triple_valid:
        count += 1
min_total = min(totals)

print(count, min_total)