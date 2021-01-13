
import sort
import numpy
from random import randint
from math import ceil
from time import time
from warnings import filterwarnings
filterwarnings("error")

fnInput = "input.txt"
P = 4
#======Variant #1======
N = 50000
M = 60
funSort = sort.bubbleSort
#======================

def generateRandomArray(count):
    with open(fnInput, "w") as f:
        for i in range(0, count):
            f.write(str(randint(-1000000, 1000000)) + '\n')

def createFiles(N, M):
    flag = True
    A = open("A.txt", "w")
    B = open("B.txt", "w")
    curFile = A
    for i in range(0, ceil(N / M)):
        arr = numpy.loadtxt(fnInput, numpy.int, skiprows=i*M, max_rows=M)
        funSort(arr)
        numpy.savetxt(curFile, arr, "%i", delimiter='\n')
        if (flag):
            curFile = B
            flag = False
        else:
            curFile = A
            flag = True
    A.close()
    B.close()

def checkIsSortedFile(fName):
    return sort.Check(numpy.loadtxt(fName, numpy.int))

def mergeFiles(input1, input2, output, size):
    flag = False
    arr1 = arr2 = []

    try:
        arr1 = numpy.loadtxt(input1, numpy.int, max_rows=M//2).tolist()
        arr2 = numpy.loadtxt(input2, numpy.int, max_rows=M//2).tolist()
        while (len(arr1) > 0 and len(arr2) > 0):
            if (arr1[0] < arr2[0]):
                output.write(str(arr1.pop(0)) + '\n')
            else:
                output.write(str(arr2.pop(0)) + '\n')
        for i in range(0, size - 1):
            if (len(arr1) == 0):
                arr1 = numpy.loadtxt(input1, numpy.int, max_rows=M//2).tolist()
            else:
                arr2 = numpy.loadtxt(input2, numpy.int, max_rows=M//2).tolist()

            while (len(arr1) > 0 and len(arr2) > 0):
                if (arr1[0] < arr2[0]):
                    output.write(str(arr1.pop(0)) + '\n')
                else:
                    output.write(str(arr2.pop(0)) + '\n')
    except Exception:
        flag = True

    try:
        if (len(arr1) != 0):
            numpy.savetxt(output, arr1, "%i", delimiter='\n')
            if (flag):
                numpy.savetxt(output, numpy.loadtxt(input1, numpy.int), "%i", delimiter='\n')
        else:
            numpy.savetxt(output, arr2, "%i", delimiter='\n')
            if (flag):
                numpy.savetxt(output, numpy.loadtxt(input2, numpy.int), "%i", delimiter='\n')
    except Exception:
        pass

    return flag

def polyPhaseMerge(M):
    size = M
    fnA = "A.txt"
    fnB = "B.txt"
    fnC = "C.txt"
    fnD = "D.txt"
    modeAB = "r"
    modeCD = "w"
    lastOutFn = fnC
    flag = True

    while (size < N):
        A = open(fnA, modeAB)
        B = open(fnB, modeAB)
        C = open(fnC, modeCD)
        D = open(fnD, modeCD)
        modeAB, modeCD = modeCD, modeAB
        if (flag):
            input1 = A
            input2 = B
            curOut = C
            lastOutFn = fnC
            flag = False
        else:
            input1 = C
            input2 = D
            curOut = A
            lastOutFn = fnA
            flag = True

        while (True):
            if (mergeFiles(input1, input2, curOut, ((size * 2) // (M // 2)) - 1)):
                break
            if (curOut == C):
                curOut = D
            elif (curOut == D):
                curOut = C
            elif (curOut == A):
                curOut = B
            else:
                curOut = A

        A.close()
        B.close()
        C.close()
        D.close()
        size *= 2

    return lastOutFn



generateRandomArray(N)

start = time()
createFiles(N, M)
fnResult = polyPhaseMerge(M)
stop = time()

chk = checkIsSortedFile(fnResult)

print("Input file: %s" % fnInput)
print("Parametrs:\n\tP = %d\n\tN = %d\n\tM = %d\n\tFunction sort: %s" % (P, N, M, funSort.__name__))
print("Result in file: %s" % fnResult)
print("Time sorting: %f" % (stop - start))
print("Is sorted: %r" % chk)
