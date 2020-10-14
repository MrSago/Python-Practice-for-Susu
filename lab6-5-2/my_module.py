
import os, re
from numpy import prod


def fileListCurDir():
    return (os.listdir(os.getcwd()))

def listPrint(lst):
    i = 0
    while (i < len(lst)):
        print("%d. %s" % (i + 1, lst[i]))
        i += 1

def outFunc(fInput, check):
    fo = open("output.txt", "w")

    if (not check):
        fo.write("Файл с входными данными не обнаружен")
        fo.close()
        return (None)

    fi = open(fInput, "r")
    inNum = re.match(r'^\d+', fi.readline()).group(0)
    fi.close()

    fo.write("Число: %s\n" % inNum)
    fo.write("Количество цифр: %d\n" % len(inNum))
    fo.write("Сумма цифр: %d\n" % sum([int(i) for i in inNum]))
    fo.write("Произведение цифр: %d\n" % prod([int(i) for i in inNum]))

    fo.close()
