l = [2, 4, 7]
sq = []
for x in l:
    if x % 2 == 0:
        result = x**2
        sq.append(result)
    if x % 2 == 1:
        result = x**3
        sq.append(result)

def squares(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num**2)
        if num % 2 == 1:
            result.append(num**3)
    return result

# print(squares([3, 4, 5]))

def sum(numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result

# print(sum([3, 4, 5]))

def perimeter(width, height):
    return 2*(width + height)
# print(perimeter(2, 4))

def area(width, height):
    return width*height
# print(area(2, 5))

# написать функцию, которая возвращает список делителей числа
def divider(b):
    result = []
    for num in range (1, b + 1):
        if b % num == 0:
            result.append(num)
    return result
# print(divider(12))

# найти сумму отрицательных чисел
def neg_sum(numbers):
    result = 0
    for num in numbers:
        if num < 0:
            result = num + result
    return result

# print(neg_sum([1, -2, 3, -4, 5, -6]))
N = 20
dividers = [num for num in range(1, N+1) if N % num == 0]
# print(dividers)

M = [1, 2, 3, 4, 5, 6]
multiplied = [num*1.1 for num in M]
# print(multiplied)

s = "Mama mila ramu"

# вернуть список слов в предложении
def words(string:str) -> list:
    result = []
    begin = 0
    end = 0
    index = 0
    for ch in string:
        end = index + 1
        if ch in ",().—:«»!\n ":
            if string[begin:end-1]:
                result.append(string[begin:end-1])
            begin = end
        index += 1
    if string[begin:end]:
        result.append(string[begin:end])
    return result
            

# print(words(s))

s = """Погода сегодня (несмотря на прогнозы) была отличная:
солнце светило ярко, птицы пели — казалось, что лето в самом разгаре!
Однако к вечеру небо затянуло тучами, и начался дождь... 
«Ну вот, — подумал я, — опять эти сюрпризы!» За окном шумел ветер,
а на подоконнике, как ни в чём не бывало, спал кот."""

print(words(s))
