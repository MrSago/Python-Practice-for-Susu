
from time import time

def Check(A):
    return all(A[i] <= A[i + 1] for i in range(len(A) - 1))

#========================
#====== Variant #1 ======
#========================

#Method #0
#Python Sort
def pySort(ptrArray):
    start = time()
    ptrArray.sort()
    return time() - start

#Method #1
#Bubble Sort
def bubbleSort(ptrArray):
    start = time()
    for i in range(len(ptrArray) - 1):
        isSwap = False
        for j in range(len(ptrArray) - 1 - i):
            first = ptrArray[j]
            second = ptrArray[j + 1]
            if (first > second):
                ptrArray[j] = second
                ptrArray[j + 1] = first
                isSwap = True
        if (not isSwap):
            break
    return time() - start

#Method #2
#Insertion Sort
def insertionSort(ptrArray):
    start = time()
    for i in range(1, len(ptrArray)):
        tmp = ptrArray[i]
        j = i - 1
        while (j >= 0 and ptrArray[j] > tmp):
            ptrArray[j + 1] = ptrArray[j]
            j -= 1
        ptrArray[j + 1] = tmp
    return time() - start

#Method #6
#Quick Sort
def quickSort(ptrArray):
    def partition(arr, low, high):
        pi = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        while (True):
            i += 1
            while (arr[i] < pi):
                i += 1
            j -= 1
            while (arr[j] > pi):
                j -= 1
            if (i >= j):
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def recQs(arr, low, high):
        while (low < high):
            p = partition(arr, low, high)
            recQs(arr, low, p - 1)
            low = p + 1

    start = time()
    recQs(ptrArray, 0, len(ptrArray) - 1)
    return time() - start
