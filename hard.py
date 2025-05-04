def add_lists(first, second):
  lists_sum = []

  min_len = min(len(first), len(second))
  max_len = max(len(first), len(second))

  for i in range(min_len):
      lists_sum.append(first[i] + second[i]) 
  
  for i in range(min_len, max_len):
    if len(first) > len(second):
      lists_sum.append(first[i])
    else:
      lists_sum.append(second[i])
  return lists_sum

#  добить эти случаи
# свести к одному случаю
# не отбрасывать концы списков
# случай с пустыми списками

print(add_lists([4], [1, 100]))

assert add_lists([], []) == [] 
assert add_lists([1, 2, 3], [3, 2, 1]) == [4, 4, 4]
assert add_lists(['aaa', 'bbb'], ['bbb', 'aaa']) == ['aaabbb', 'bbbaaa']
assert add_lists([7, 2, 3, 12, 121], [1, 4]) == [8, 6, 3, 12, 121]
assert add_lists([4], [1, 100]) == [5, 100]

