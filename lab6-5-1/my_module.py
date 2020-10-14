
import re, numpy as np


def getInput():
    f = open("input.txt", "r")
    str1 = f.readline()
    str2 = f.readline()
    f.close()

    res = [int(i) for i in re.findall(r'\d+', str1)[:2]]
    if (len(res) == 0):
        print("Размерность не найдена!")
        return (res)

    try:
        res.append(re.match(r'^\w+.txt', str2).group(0))
    except AttributeError:
        print("Не найдено имя файла!")
        res.clear()

    return (res)

def PrintRectangle(a, b, file):
    m = np.ones((b, a))
    m[1:-1, 1:-1] = 0

    f = open(file, "w")
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (m[i][j]):
                f.write('*')
            else:
                f.write(' ')
        f.write('\n')
    f.close()


def PrintSquare(a, file):
    PrintRectangle(a, a, file)
