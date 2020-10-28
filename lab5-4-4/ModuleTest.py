
from function import fun
from prettytable import PrettyTable


def simpleTest(sum):
    res = fun(sum)
    return (res)

def moduleTest(a, b, step):
    try:
        a = int(a)
        b = int(b)
        step = int(step)
    except ValueError:
        return ("Неверно введены значения")
    if (a > b or step <= 0):
        return ("Неверные условия теста!")

    resTable = PrettyTable()
    resTable.field_names = ["INPUT", "OUTPUT"]

    i = a
    while (i <= b):
        resTable.add_row([i, fun(i)])
        i += step

    res = resTable.get_string()
    return (res)
