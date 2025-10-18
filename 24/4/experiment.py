original = "Ф2025Б2025В2025Г"

cutted = original.split("2025")
print(cutted)

print(total := '2025' + "2025".join(cutted))
print(original)