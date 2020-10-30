
import os, re
from time import time


def fileListCurDir():
    return (os.listdir(os.getcwd()))

def listPrint(lst):
    i = 0
    while (i < len(lst)):
        print("%d. %s" % (i + 1, lst[i]))
        i += 1

#Решето Эратосфена
def primeNums(N):
    num = int(N)
    pr = []
    lp = [0 for i in range(0, num + 1)]

    i = 2
    while (i <= num):
        if (lp[i] == 0):
            lp[i] = i
            pr.append(i)
        for p in pr:
            if (p <= lp[i] and p*i <= num):
                lp[p*i] = p
            else:
                break
        i += 1

    return (pr)

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

        print("Вычисление простых чисел до: %s" % inNum)
        start = time()
        res = primeNums(inNum)
        stop = time()

        for i in res:
            #print(i, end=' ')
            fo.write(str(i) + ' ')
        #print("")

    print("Время вычисления: %f сек." % (stop - start))
    print("Результат записан в файл: \"%s\"" % fOutput)
