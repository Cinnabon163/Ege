count = 0
for N in range(100000000, 1000000000):
    binary_N = bin(N)
    bin_mod_N = bin(N % 4)
    R = binary_N + bin_mod_N[2:]
    R = int(R, 2)
    if 1_000_000_000 <= R <= 1_789_456_123:
        count +=1
    if R > 1_789_456_123:
        print('Done')
        break
print(R)
print(count)

