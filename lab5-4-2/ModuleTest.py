
from function import fun
from prettytable import PrettyTable


def simpleTest(A, B, C):
    fRes = fun(A, B, C)
    if (fRes[1] != "-" and fRes[2] != "-"):
        count = 2
    elif (fRes[2] == "-"):
        count = 1
    else:
        count = 0
    res = "Уравнение\n" + fRes[0] + "\nКоличество корней: " + str(count) + '\n' + str(fRes[1]) + '\n' + str(fRes[2])
    return (res)

def moduleTest(a, b, step):
    try:
        a = float(a)
        b = float(b)
        step = float(step)
    except ValueError:
        return("Неверно введены значения")
    if (a > b or step <= 0):
        return("Неверные условия теста!")

    resTable = PrettyTable()
    resTable.field_names = ["Ax^2+Bx+C=0", "x1", "x2"]

    i = j = k = a
    while (i <= b):
        while (j <= b):
            while (k <= b):
                fRes = fun(i, j, k)
                resTable.add_row([fRes[0], fRes[1], fRes[2]])
                k += step
            j += step
            k = a
        i += step
        j = a

    res = "\nДиапазон: [%g; %g]\nШаг: %g\n" % (a, b, step) + resTable.get_string()
    return (res)
