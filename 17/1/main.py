f = open("data/17.txt", "r")
# print(f.readline())
f.close()

lines = []
with open("data/17.txt", "r") as f:
    lines = f.readlines()
    
def is_positive(str_num):
    return str_num[0] != '-'

def is_negative(str_num):
    return str_num[0] == '-'

def is_pair_have_same_digit(sn1, sn2):
    if is_positive(sn1) and is_positive(sn2):
        return True
    if is_negative(sn1) and is_negative(sn2):
        return True
    return False

count = 0
for index, _ in enumerate(lines[1:], 1):
    if is_pair_have_same_digit(lines[index], lines[index-1]):
        count += 1

print(count)