nums = [int(x) for x in open('17.txt')]

min_num = min(x for x in nums if abs(x) % 10 == 3)
count = 0
max_sum = -10**10

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    m = min(a, b)
    if abs(m) % 10 == 3:
        s = a**2 + b**2
        if s < min_num**2:
            count += 1
            if s > max_sum:
                max_sum = s
print(max_sum)
