# https://inf-ege.sdamgia.ru/problem?id=33198
# f = open("26.txt")
# N, M = map(int, f.readline().strip().split(' '))
# priority = 0
# usual = []
# for line in f.readlines():
#     weight = int(line)
#     if 200 <= weight <= 210:
#         priority += weight
#     else:
#         usual.append(weight)

# M -= priority

# usual.sort(reverse=True)

def get_variants(usual, M):
    variants = []

    l = len(usual)
    k = 0

    for i in range(l):
        var = []
        for j in range(i,l):
            if sum(var) + usual[j] > M:
                continue
            else:
                var.append(usual[j])
        variants.append(var)
        
    return variants

usual = [7,6,3,3,2,1]
variants = get_variants(usual, 10)
sums = [sum(var) for var in variants]
max_w = max(sums)

top_vars = [var for var in variants if sum(var) == max_w]

print(get_variants(usual, 10))

        



# M = 10

# 7,6,3,3,2,1

# 7 + 3
# 6+3+1
# 7+2+1

# f.close()
