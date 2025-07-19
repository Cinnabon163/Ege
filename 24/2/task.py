content = ""
with open("data/24.txt") as f:
    content = f.read()

letters = ['A', 'B', 'C', 'D', 'E', 'F']

count = 0

def test(triple:tuple):
    if triple[0] in ['A', 'B', 'C']:
        if triple[1] in ['C', 'D', 'E']:
            if triple[2] not in ['A', 'E']:
                if triple[0] != triple[1] and triple[0] != triple[2] and triple[1] != triple[2]:
                    return True
    return False

for i,_ in enumerate(content[2:], 2):
    triple = (content[i], content[i-1], content[i-2])
    if test(triple):
        count += 1
        
print(count)
