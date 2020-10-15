
from math import sqrt


def fun(A, B, C):
    res = {"A": "-", "B": "-", "C": "-", "x1": "-", "x2": "-"}

    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        return (res)

    round(A, 5)
    round(B, 5)
    round(C, 5)

    res["A"] = "%0.5f" % A
    res["B"] = "%0.5f" % B
    res["C"] = "%0.5f" % C

    if (not A):
        return (res)

    D = B**2 - 4*A*C

    if (D > 0):
        res["x1"] = "%0.5f" % ((-B + sqrt(D)) / (2*A))
        res["x2"] = "%0.5f" % ((-B - sqrt(D)) / (2*A))
    elif (D == 0):
        res["x1"] = "%0.5f" % (-B / (2*A))

    return (res)
