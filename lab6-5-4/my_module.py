
import os, re
from time import time
from datetime import datetime


def fileListCurDir():
    return (os.listdir(os.getcwd()))

def listPrint(lst):
    i = 0
    while (i < len(lst)):
        print("%d. %s" % (i + 1, lst[i]))
        i += 1

def fun(R, x, y):
    count = 0
    R_kv = R**2

    for i in range(x-R, x):
        for j in range(y-R, y):
            x_i_kv = (x-i)**2
            if (x_i_kv + (y-j)**2 <= R_kv):
                count += 1

    count = (count * 4) + ((R * 4) + 1)

    return (count)

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
                str1 = fi.readline()
                str2 = fi.readline()
        except IOError:
            print("Ошибка чтения файла: \"%s\"" % fInput)
            fo.write("Ошибка чтения файла: \"%s\"" % fInput)
            return

        try:
            res = [int(re.match(r'^\d+$', str1).group(0))]
            res += [int(i) for i in re.match(r'^\d+ \d+$', str2).group(0).split()]
        except AttributeError:
            print("Данные в файле не найдены!")
            fo.write("Данные в файле не найдены!")
            return;

        start = time()
        resFun = fun(res[0], res[1], res[2])
        stop = time()

        resStr = datetime.now().strftime("%d.%m.%Y %H:%M") + '\n' + str(resFun) + '\n' + str('%f' % (stop - start))
        fo.write(resStr)


    print("Данные из файла: R=%d (%d;%d)" % (res[0], res[1], res[2]))
    print(resStr)
    print("Результат записан в файл: \"%s\"" % fOutput)
