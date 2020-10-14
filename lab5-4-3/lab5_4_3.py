
print("Variant #3")
print("Введите время отправления поезда и время в пути в формате:")
print("Hotp - время отправления (часы)")
print("Motp - время отправления (минуты)")
print("Hp - время в пути (часы)")
print("Mp - время в пути (минуты)")

Hotp = input()
Motp = input()
Hp = input()
Mp = input()

try:
    Hotp = int(Hotp)
    Motp = int(Motp)
    Hp = int(Hp)
    Mp = int(Mp)
except ValueError:
    print("Одно из значений не является целым числом!")
    exit(0)

if (Hotp < 0 or Hotp >= 24 or Motp < 0 or Motp >= 60):
    print("Время отправления выходит из диапазона: Hotp[0;24) и Motp[0;60)")
    exit(0)

if (Hp < 0 or Mp < 0):
    print("Время в пути не может быть отрицательным")
    exit(0)


Msum = Motp + Mp
Hsum = Hotp + Hp + (Msum // 60)

Mres = Msum % 60
Hres = Hsum % 24

Dres = (Hp + (Mp // 60)) // 24

print("%s hours : %s minutes" % ('{:02}'.format(Hres), '{:02}'.format(Mres)))
print("%d days" % Dres)
