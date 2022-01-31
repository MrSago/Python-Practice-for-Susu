
print("Лабораторная работа lab3-5")
print("Введите данные")
sName = input("Фамилия: ")
fName = input("Имя: ")
group = input("Группа: ")

print("Привет, %s %s из группы %s" % (sName, fName, group))
email = input("Введи свою электронную почту?\n")

print((sName[:5] + fName[:5] * 2 + email[:5] * 3).lower())

