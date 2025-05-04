from pprint import pprint



words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_place = dict()
for word in words:
    if word in word_place:
        word_place[word] += 1
    else:
        word_place[word] = 1

grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "Dana": 65}  

filtered_grades = {}

for name, grade in grades.items():
    if grade > 75:
        filtered_grades[name] = grade

university = {
    "CS": {"students": 150, "courses": ["Python", "Algorithms"]},
    "Math": {"students": 80, "courses": ["Calculus", "Algebra"]}
}
university["physics"] = {"students": 50, "courses": ["Engeneering", "Nuclear physics"]}


#- Напишите функцию, которая инвертирует словарь 
# (ключи → значения, значения → ключи). Учтите, что 
# значения должны быть неизменяемыми.  

def invert_dic_new(d):
    inverted_dic = {}
    for key, value in d.items():
        inverted_dic[value] = key
    return inverted_dic
    

library = {
    "Гарри Поттер": {"автор": "Дж. Роулинг", "жанр": "фэнтези"},
    "1984": {"автор": "Оруэлл", "жанр": "антиутопия"},
    "Скотный двор": {"автор": "Оруэлл", "жанр": "антиутопия"},
    "Хроники Нарнии": {"автор": "Стивенсон", "жанр": "фэнтези"},
    # ...
}

def add_book(library, heading, author, genre):
    if heading in library:
        return False
    library[heading] = {"автор": author, "жанр": genre}
    return True
    
add_book(library=library, heading="Том Сойер", author="Марк Твен", genre="приключения")

# возвращает СПИСОК названий книг заданного автора
def find_by_author(library, author):
    books = []
    for heading, value in library.items():
        if value["автор"] == author:
            books.append(heading)
    return books

# вернуть список книг заданного жанра
def find_by_genre(library, genre):
    books = []
    for heading, value in library.items():
        if value["жанр"] == genre:
            # "Хроники Нарнии": {"автор": "Стивенсон", "жанр": "фэнтези"}  
            books.append({heading: value})
    return books
fantacy_books = find_by_genre(library, "фэнтези")
print (fantacy_books)

        
    
    
    
