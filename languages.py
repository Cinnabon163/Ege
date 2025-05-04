# Верните список языков, где ваш балл составляет не менее 60, в порядке убывания баллов.
def my_languages(results):
    filtered_grades = []

    for name, grade in results.items():
        if grade > 60:
            filtered_grades.append(name)
    return filtered_gradesred_grades


grades = {"Java": 10, "Ruby": 65, "Python": 80, "Go": 70}
result = my_languages(grades)# ["Ruby", "Python"]
print(result)