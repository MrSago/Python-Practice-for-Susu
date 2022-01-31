
def fun(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return (-1)

    if ((a <= 0 or b <= 0 or c <= 0) or (a + b <= c or a + c <= b or b + c <= a)):
        return (0) #не существует
    elif ((a == b) and (a == c)):
        return (1) #равносторонний
    elif ((a == b) or (a == c) or (b == c)):
        return (2) #равнобедренный
    else:
        return (3) #общего вида

