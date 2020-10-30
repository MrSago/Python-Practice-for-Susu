
import re, numpy as np


def getInputFromFile(fInput):
    try:
        with open(fInput, "r") as f:
            str1 = f.readline()
            str2 = f.readline()
    except IOError:
        print("Ошибка чтения файла: \"%s\"" % fInput)
        return (list())

    res = [int(i) for i in re.findall(r'\d+', str1)[:2]]
    if (len(res) == 0):
        print("Размерность не найдена!")
        return (res)

    try:
        res.append(re.match(r'^\w+.txt', str2).group(0))
    except AttributeError:
        print("Не найдено имя файла!")
        res.clear()
    finally:
        print("Данные из файла \"%s\": %s" % (fInput, str(res)))
    return (res)

def PrintRectangle(a, b, fOutput):
    m = np.ones((b, a))
    m[1:-1, 1:-1] = 0

    try:
        with open(fOutput, "w") as f:
            for i in range(len(m)):
                m_save = m[i]
                for j in range(len(m_save)):
                    if (m_save[j]):
                        f.write('*')
                    else:
                        f.write(' ')
                f.write('\n')
    except IOError:
        print("Ошибка записи в файл: \"%s\"" % fOutput)

def PrintSquare(a, fOutput):
    PrintRectangle(a, a, fOutput)
