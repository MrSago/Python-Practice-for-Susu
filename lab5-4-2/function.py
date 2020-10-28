
from math import sqrt


def fun(A, B, C):
    res = {"A": "-", "B": "-", "C": "-", "x1": "-", "x2": "-"}

    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        return (res)

    A = round(A, 5)
    B = round(B, 5)
    C = round(C, 5)

    res["A"] = "%0.5f" % (A)
    res["B"] = "%0.5f" % (B)
    res["C"] = "%0.5f" % (C)

    if (not A):
        return (res)

    D = B**2 - 4*A*C

    if (D > 0.0):
        sqD = sqrt(D)
        A2 = 2*A

        x1 = (-B + sqD) / A2
        x1 = round(x1, 5)
        if (x1 == -0.00000):
            x1 = 0.0

        x2 = (-B - sqD) / A2
        x2 = round(x2, 5)
        if (x2 == -0.00000):
            x2 = 0.0

        res["x1"] = "%0.5f" % (min(x1, x2))
        res["x2"] = "%0.5f" % (max(x1, x2))
    elif (D == 0.0):
        x1 = -B / (2*A)
        x1 = round(x1, 5)
        if (x1 == -0.0000):
            x1 = 0.0
        res["x1"] = "%0.5f" % (x1)

    return (res)
