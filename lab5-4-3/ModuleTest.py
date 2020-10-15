
from function import fun
import random


def simpleTest(Hotp, Motp, Hp, Mp):
    res = fun(Hotp, Motp, Hp, Mp)
    return (res)

def moduleTest():
    Hotp = random.randint(0, 23)
    Motp = random.randint(0, 59)
    Hp = random.randint(0, 100)
    Mp = random.randint(0, 100)
    res = "Hotp = %d\nMotp= %d\nHp = %d\nMp = %d\n" % (Hotp, Motp, Hp, Mp) + fun(Hotp, Motp, Hp, Mp)
    return (res)
