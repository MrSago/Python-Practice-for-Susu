
from function import fun
from prettytable import PrettyTable


def funRes(res):
    if (res == -1):
        return ("Неверно введены значения")
    elif (res == 0):
        return ("Треугольник не существует")
    elif (res == 1):
        return ("Треугольник равносторонний")
    elif (res == 2):
        return ("Треугольник равнобедренный")
    elif (res == 3):
        return ("Треугольник общего вида")
    else:
        return (None)

def simpleTest(a, b, c):
    res = funRes(fun(a, b, c))
    return (res)

def moduleTest(a, b, step):
    try:
        a = float(a)
        b = float(b)
        step = float(step)
    except ValueError:
        return ("Неверно введены значения")
    if (a > b or step <= 0):
        return ("Неверные условия теста!")

    resTable = PrettyTable()
    resTable.field_names = ["a", "b", "c", "Вид треугольника"]

    i = j = k = a
    while (i <= b):
        while (j <= b):
            while (k <= b):
                resTable.add_row([i, j, k, funRes(fun(i, j, k))])
                k += step
            j += step
            k = a
        i += step
        j = a

    res = "\nДиапазон: [%g; %g]\nШаг: %g\n" % (a, b, step) + resTable.get_string()
    return (res)
