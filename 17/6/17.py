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

assert max36 % 36 == 0

def is_positive(x):
    x = int(x)
    return x > 0

def endswith_36(x):
    return str(x).rstrip()[-2:] == "36" # нужно удалить \n с конца

assert endswith_36("1236") == True
assert endswith_36("-1236") == True
assert endswith_36("23343") == False
assert endswith_36("-99536\n") == True # вот пример того что приходит из файла


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
    is_count_valid = count >= 2
    is_total_valid = total <= max36
    is_valid = is_count_valid and is_total_valid
    # if total == -175325:
    #     print(current, prev, prev_prev)
    return (is_valid, total)

triple_good = (str(35), str(-36), str(36))
assert get_triple_status(*triple_good, max36=max36) == (True, 35-36+36)

triple_bad = ("8772", "-84561", "-99536") # total = -175325
assert get_triple_status(*triple_bad, max36=max36) == (True, -175325)

count = 0
totals = []
for i, _ in enumerate(content[2:], 2):
    triple = (content[i], content[i-1], content[i-2])
    if triple[0].strip() == "8772":
        print(triple)
    status = get_triple_status(*triple, max36)
    is_triple_valid = status[0]
    if is_triple_valid:
        totals.append(status[1]) # тут не было условия проверки валидности тройки
        count += 1
        
min_total = min(totals)

print(count, min_total)