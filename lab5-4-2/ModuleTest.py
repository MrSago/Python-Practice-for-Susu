
from function import fun
from prettytable import PrettyTable


def simpleTest(A, B, C):
    fRes = fun(A, B, C)
    if (fRes["x1"] != "-" and fRes["x2"] != "-"):
        count = 2
    elif (fRes["x1"] != "-"):
        count = 1
        fRes["x2"] = ""
    else:
        count = 0;
        fRes["x1"] = ""
        fRes["x2"] = ""

    res = "Уравнение\n(%s)x^2+(%s)x+(%s)=0" % (fRes["A"], fRes["B"], fRes["C"]) + "\nКоличество корней: " + str(count)
    if (count == 2):
        res += '\n' + str(fRes["x1"]) + '\n' + str(fRes["x2"])
    elif (count == 1):
        res += '\n' + str(fRes["x1"]) 

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
    resTable.field_names = ["A", "B", "C", "x1", "x2"]

    i = j = k = a
    while (i <= b):
        while (j <= b):
            while (k <= b):
                fRes = fun(i, j, k)
                resTable.add_row([fRes["A"], fRes["B"], fRes["C"], fRes["x1"], fRes["x2"]])
                k += step
            j += step
            k = a
        i += step
        j = a

    res = "\nДиапазон: [%g; %g]\nШаг: %g\n" % (a, b, step) + resTable.get_string()
    return (res)
