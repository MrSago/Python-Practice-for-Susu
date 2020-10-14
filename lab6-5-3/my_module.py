
import os, re


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

    for i in simpleNums(int(inNum)):
        fo.write(str(i) + ' ')

    fo.close()

def simpleNums(N):
    nums = [2]
    for num in range(3, N, 2):
        if all(num % i != 0 for i in range(3, num, 2)):
            nums.append(num)
    return (nums)
