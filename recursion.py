import sys
from functools import lru_cache

sys.setrecursionlimit(200000)


def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total = total + sum_nested(item)
        else:
            total = total + item
    return total
    
print(sum_nested([1, [2, [3, [4]]]])) # 10
print(sum_nested([5, [5, [5, [5]]]])) # 20

nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
print(sum_nested(nested_list)) # 55

l = []
with open("sfsdfsd.txt", "r") as f:
    l = f.readlines()