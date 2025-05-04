# на вход подается список из кортежей со словами. Требуется вывести кортеж
# в котором указаны самые длинные слова в кортеже. Если слова одинаковой длины,
# их нужно упаковать в кортеж и вывести на соответствующей позиции.

# '''
# 1. нужно узнать какое слово в кортеже самое длинное и получить его расположение(индекс)
#     1.1. нужно составить список, в котором будут длины каждого слова
#     1.2. узнаём индексы max значений
#         1.2.1. узнать само max значение
#         1.2.2. выковырять индексы
#     1.3. сложить в список, не забыв обработать случай с несколькими максимумами
# '''

def get_list_longest_words(tup_list) -> tuple:
    result = []

    for tup in tup_list:
        words = get_tup_longest_words_by_positions(tup)
        if len(words) > 1:
            result.append(tuple(words))
        else:
            result.append(words[0])
    return tuple(result)
        

# ВЕРНУТЬ длиннейшие слова по их позициям   
def get_tup_longest_words_by_positions(tup:tuple) -> list:
    longest_words = []
    positions = get_longest_words_positions(tup)
    for pos in positions:
        longest_words.append(tup[pos])
    return longest_words

# ВЕРНУТЬ позиции длиннейших слов в кортеже

def get_tup_lngths(tup) -> list:
    lengths = []

    for word in tup:
        length = len(word)
        lengths.append(length)
    return lengths

assert get_tup_lngths(("aaaa", "b", "ccc")) == [4, 1, 3]
assert get_tup_lngths(()) == []

def get_tup_max_len(lengths:list) -> int:
    max_len = 0
    for l in lengths:
        if l > max_len:
            max_len = l
    return max_len

assert get_tup_max_len(lengths=[3, 5, 7]) == 7
assert get_tup_max_len(lengths=[]) == 0

def get_words_lengths(tup):
    lengths = []

    for word in tup:
        length = len(word)
        lengths.append(length)
    return lengths

assert get_words_lengths(("Cat and dog", "Dog and cat", "cat")) == [11, 11, 3]

def get_longest_word_length(lengths):
    max_len = 0
    for l in lengths:
        if l > max_len:
            max_len = l
    return max_len

def get_index_longest_length(lengths, max_len):
    positions = []
    for index in range(len(lengths)):
        if lengths[index] == max_len:
            positions.append(index)

    return positions

def get_longest_words_positions(tup):
    # lengths - длины строк в кортеже
    lengths = get_words_lengths(tup)
    # наход макс длину строчки в кортеже
    max_len = get_longest_word_length(lengths)
    # наход индекса макс длины строки
    return get_index_longest_length(lengths, max_len)

sl = [
    ("orange", "apple", "banana"),
    ("Canada", "Australia", "New Zeland", "Namibia"),
    ("копейка", "казахский")
]

result = get_longest_words_positions(sl[1]) # [0, 2]
print(result)


assert get_list_longest_words(sl) == (("orange", "banana"), "New Zeland", "казахский")

