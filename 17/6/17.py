content = []
with open("data/17.txt") as f:
    content = f.readlines()

# найти максимальный элемент в последовательности, кратный 36
multiples_of_36 = []
for str_num in content:
    num = int(str_num)
    if num % 36 == 0:
        multiples_of_36.append(num)

max36 = max(multiples_of_36)

assert max36 % 36 == 0

def is_positive(x):
    x = int(x)
    return x > 0

def endswith_36(x):
    return str(x)[-2:] == "36"

assert endswith_36("1236") == True
assert endswith_36("-1236") == True
assert endswith_36("23343") == False


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
    return (count >= 2 and total <= max36, total)

triple_good = (str(35), str(-36), str(36))
assert get_triple_status(*triple_good, max36=max36) == (True, 35-36+36)

triple_bad = (str(35), str(-36), str(-39))
assert get_triple_status(*triple_bad, max36=max36) == (False, 35-36-39)

count = 0
totals = []
for i, _ in enumerate(content[2:], 2):
    triple = (content[i], content[i-1], content[i-2])
    status = get_triple_status(*triple, max36)
    is_triple_valid = status[0]
    totals.append(status[1])
    if is_triple_valid:
        count += 1
min_total = min(totals)

print(count, min_total)