
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
    with open(fOutput, "w") as fo:
        if (fInput in fList):
            print("\"%s\" присутствует в текущей директории!" % fInput)
        else:
            print("Файл с входными данными не обнаружен")
            fo.write("Файл с входными данными не обнаружен")
            return

        try:
            with open(fInput, "r") as fi:
                inStr = fi.readline()
        except IOError:
            print("Ошибка чтения файла: \"%s\"" % fInput)
            fo.write("Ошибка чтения файла: \"%s\"" % fInput)
            return

        try:
            inNum = re.match(r'^\d+', inStr).group(0)
        except AttributeError:
            print("Число в файле не найдено!")
            fo.write("Число в файле не найдено!")
            return

        res = aboutNum(inNum)
        fo.write(res)

    print(res)
    print("Результат записан в файл: \"%s\"" % fOutput)
