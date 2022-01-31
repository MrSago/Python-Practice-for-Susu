
from math import exp, sqrt

def fun(x):
    try:
        x = float(x)
    except ValueError:
        return ("[NaN]")

    if (x <= 0):
        return ("[out of range]")

    return (str(exp(sqrt(x+sqrt(x)))))

