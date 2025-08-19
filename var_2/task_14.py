a = 49**10 + 7**30 - 49
t = ''
while a > 0:
    t = str(a % 7) + t
    a = a//7
print(t.count('6'))
print(t)

n = 49**10 + 7**30 - 49
count = 0
while n > 0:
    if n % 7 == 6:
        count += 1
    n//=7
    
print(count)
    