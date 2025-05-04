content = []
with open("data/17.txt") as f:
   content = f.readlines()
# print(content)

def is_even(str_number):
   return int(str_number) % 2 == 0

def is_odd(str_number):
    return not is_even(str_number)
 
def num_pair_have_same_pairity(str_first, str_second):
   if is_even(str_first) and is_even(str_second):
      return True
   if is_odd(str_first) and is_odd(str_second):
      return True
   return False

count = 0
for index, _ in enumerate(content[1:], 1):
   if num_pair_have_same_pairity(content[index], content[index-1]):
      count += 1
      
count = 0
prev = content[0]
for _, value in enumerate(content[1:], 1):
   if num_pair_have_same_pairity(value, prev):
      count += 1
   prev = value

# print(count)






