
from prettytable import PrettyTable

priziv = []

print("Лабораторная работа lab4-5")
print("Введите данные о 5-ти призывниках в формате:")
print("Фамилия\nИмя\nОтчество\nГод Рождения\nЗаболевание\n")
for i in range(0, 5):
    print("\nПризывник №%d:" % (i + 1))
    priziv.append({
        "id":           i,
        "Фамилия":      input(),
        "Имя":          input(),
        "Отчество":     input(),
        "Год Рождения": input(),
        "Заболевание":  input()
    })

table = PrettyTable()
table.field_names = ["№", "Фамилия", "Имя", "Отчество", "Год Рождения", "Заболевание"]
for i in priziv:
    table.add_row([
        str(i.get("id") + 1),
        i.get("Фамилия"),
        i.get("Имя"),
        i.get("Отчество"),
        i.get("Год Рождения"),
        i.get("Заболевание")
    ])

print(table)
