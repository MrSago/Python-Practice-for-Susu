
from function import fun
from random import randint


def simpleTest(Hotp, Motp, Hp, Mp):
    res = fun(Hotp, Motp, Hp, Mp)
    return (res)

def moduleTest():
    Hotp = randint(0, 23)
    Motp = randint(0, 59)
    Hp = randint(0, 100)
    Mp = randint(0, 100)
    res = "Hotp = %d\nMotp= %d\nHp = %d\nMp = %d\n" % (Hotp, Motp, Hp, Mp) + fun(Hotp, Motp, Hp, Mp)
    return (res)
