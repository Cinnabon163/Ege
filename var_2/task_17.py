import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '17.txt')

numbers = []
with open (filename) as f:
    nums = f.readlines()
    numbers = [int(n.strip()) for n in nums]

count = 0
maxsum = -1
for index, _ in enumerate(numbers[1:], 1):
    cur = numbers[index]
    prev = numbers[index-1]
    
    pr_mod_10 = cur*prev % 10 == 0
    
    if pr_mod_10:
        count += 1
        s = cur + prev
        if s > maxsum:
            maxsum = s

print(count, maxsum)
            

