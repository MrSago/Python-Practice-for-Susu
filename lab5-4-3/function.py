
def fun(Hotp, Motp, Hp, Mp):
    try:
        Hotp = int(Hotp)
        Motp = int(Motp)
        Hp = int(Hp)
        Mp = int(Mp)
    except ValueError:
        return ("Одно из значений не является целым числом!")

    if (Hotp < 0 or Hotp >= 24 or Motp < 0 or Motp >= 60):
        return ("Время отправления выходит из диапазона: Hotp[0;24) и Motp[0;60)")

    if (Hp < 0 or Mp < 0):
        return ("Время в пути не может быть отрицательным")

    Msum = Motp + Mp
    Hsum = Hotp + Hp + (Msum // 60)

    Mres = Msum % 60
    Hres = Hsum % 24

    Dres = (Hsum + (Msum // 60)) // 24

    return ("%s hours : %s minutes" % ('{:02}'.format(Hres), '{:02}'.format(Mres)) + "\n%d days" % Dres)
