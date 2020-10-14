
from math import sqrt

def fun(A, B, C):
    res = ["Ax^2+Bx+C=0", "x1", "x2"]

    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        res[:] = "-"
    if (not A):
        res[0] = "(0)x^2+(%.5f)x+(%.5f)=0" % (B, C)
        res[1:3] = "-"
        return (res)

    round(A, 5)
    round(B, 5)
    round(C, 5)

    D = B**2 - 4*A*C

    if (D > 0):
        #print("Количество корней: 2")
        res[1] = (-B + sqrt(D)) / (2*A)
        res[2] = (-B - sqrt(D)) / (2*A)
    elif (D == 0):
        #print("Количество корней: 1")
        res[1] = -B / (2*A)
        res[2] = "-"
    else:
        #print("Количество корней: 0")
        res[1] = "-"
        res[2] = "-"

    res[0] = "(%.5f)x^2+(%.5f)x+(%.5f)=0" % (A, B, C)
    return (res)
