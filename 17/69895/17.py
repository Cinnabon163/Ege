nums = [int(x) for x in open('17.txt')]

min_elem = min(nums)
count = 0
max_sum = -1

for i in range(len(nums) - 1):
    a,b = nums[i], nums[i + 1]
    if (a % 18 + b % 18) == min_elem:
        count += 1
        if a + b > max_sum:
            max_sum = a+b
print(max_sum)