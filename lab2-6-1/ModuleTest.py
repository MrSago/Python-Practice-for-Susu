
from function import fun
from prettytable import PrettyTable


def simpleTest(x):
    res = fun(x)
    return ("y = exp^(sqrt(%s+sqrt(%s))) = %s" % (x, x, res))

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
    resTable.field_names = ["x", "y"]

    i = a
    while (i <= b):
        resTable.add_row(["%.5f" % i, "%.5f" % float(fun(i))])
        i += step

    res = "\nДиапазон: [%g; %g]\nШаг: %g\n" % (a, b, step) + resTable.get_string()
    return (res)
