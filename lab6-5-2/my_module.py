
import os, re
from numpy import prod


def fileListCurDir():
    return (os.listdir(os.getcwd()))

def listPrint(lst):
    i = 0
    while (i < len(lst)):
        print("%d. %s" % (i + 1, lst[i]))
        i += 1

def aboutNum(N):
    return(
        "Число: %s\n" % N +
        "Количество цифр: %d\n" % len(N) +
        "Сумма цифр: %d\n" % sum([int(i) for i in N]) +
        "Произведение цифр: %d" % prod([int(i) for i in N])
    )

def outRes(fList, fInput, fOutput):
    fo = open(fOutput, "w")

    if (fInput in fList):
        print("\"%s\" присутствует в текущей директории!" % fInput)
    else:
        print("Файл с входными данными не обнаружен")
        fo.write("Файл с входными данными не обнаружен")
        fo.close()
        return;


    fi = open(fInput, "r")
    inStr = fi.readline()
    fi.close()

    try:
        inNum = re.match(r'^\d+', inStr).group(0)
    except AttributeError:
        print("Число в файле не найдено!")
        fo.write("Число в файле не найдено!")
        fo.close()
        return;

    res = aboutNum(inNum)

    fo.write(res)
    fo.close()

    print(res)
    print("Результат записан в файл: \"%s\"" % fOutput)
