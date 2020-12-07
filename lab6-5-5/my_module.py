
import os, re, numpy as np
from random import randint

def fileListCurDir():
    return (os.listdir(os.getcwd()))

def listPrint(lst):
    i = 0
    while (i < len(lst)):
        print("%d. %s" % (i + 1, lst[i]))
        i += 1

def matrix_print(matrix, name, sz1, sz2):
    print("===================================================")
    print("Matrix %s[%d][%d]:" % (name, sz1, sz2))
    print(matrix)
    print("===================================================\n")

def matrix_fun(N, M):
    np.set_printoptions(precision=3, linewidth=200, suppress=True)
    
    A = np.random.randint(-10.0, 10.0, (N, M))
    matrix_print(A, "A", N, M)
    np.savetxt("A.txt", A, fmt="%i")
    
    new_A = np.empty((N, M))
    for i in range(0, N):
        tmpA = A[i]
        tmpnA = new_A[i]
        tmpMax = np.max(tmpA)
        if (tmpMax == 0):
            continue
        for j in range(0, M):
            tmpnA[j] = tmpA[j] / tmpMax
    matrix_print(new_A, "new_A", N, M)
    
    K = randint(5, 15)
    B = np.random.randint(-10.0, 10.0, (M, K))
    np.savetxt("B.txt", B, "%i")
    matrix_print(B, "B", M, K)
    
    prod = np.dot(new_A, B)
    np.savetxt("prod.txt", prod, "%.3f")
    matrix_print(prod, "prod", N, K)

def outRes(fList, fInput):
    if (fInput in fList):
        print("\"%s\" присутствует в текущей директории!" % fInput)
    else:
        print("Файл с входными данными не обнаружен")
        return
    
    try:
        with open(fInput, "r") as fi:
            inNum = [int(i) for i in re.findall(r'\d+', fi.readline())]
    except IOError:
        print("Ошибка чтения файла: \"%s\"" % fInput)
        return
    except ValueError:
        print("Значения не являются целыми числами!")
        return
    if (len(inNum) != 2):
        print("Неверное количество аргументов")
        return
    
    try:
        matrix_fun(inNum[0], inNum[1])
    except Exception as ex:
        print("Вызвано исключение: %s" % str(ex))
        return

    print("Результаты записаны в файлы: A.txt, B.txt, prod.txt")
