
from math import exp, sqrt


def fun(a):
    try:
        a = float(a)
    except ValueError:
        return ("[NaN]")

    if (a <= 0):
        return ("[out of range]")

    return (str(a * (1/12) * sqrt(3) * (3 + sqrt(5))))
