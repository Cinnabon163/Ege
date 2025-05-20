content = ""
with open("./data/24.txt") as f:
    content = f.read()


test_content = "ASCMJODOGDFHKJYDOGDOGZXCDOGDOGDOGDSS"


def find_next_dog(text, offset):
    return text.find("DOG", offset)

#нужно найти самую длинную собаку
longest_dog = 0
pos = 0
prev_pos = 0
current_dog = 1

while True:
    pos = find_next_dog(content, prev_pos+3)
    
    if pos == prev_pos + 3:
        current_dog += 1
        print(current_dog)
    else:
        current_dog = 1
    prev_pos = pos
    
    if current_dog > longest_dog:
        longest_dog = current_dog
        
    if pos == -1:
        break

print(longest_dog)
