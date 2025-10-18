content = ""
with open("data/24.txt") as f:
    content = f.read().split('2025')

count = 0
good = ""
lgi = 0
for i in range(len(content) - 60):
    ct = '2025' + '2025'.join(content[i:i + 60])
    if ct.count('Y') >= 120:
        if count < len(ct) + 3:
            good = ct
            lgi = i
            count = len(ct) + 3

# print(count)
sl = content[lgi:lgi+60]
print(sl)
print(concatenated := "2025" + "2025".join(sl))
print(len(concatenated), concatenated.count("2025"))
print(good == concatenated)


    
 


