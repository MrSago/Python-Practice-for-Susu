
from time import time

def Check(A):
    return all(A[i] <= A[i + 1] for i in range(len(A) - 1))

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

#Method 3
#Selection Sort
def selectionSort(ptrArray):
    start = time()
    for i, val in enumerate(ptrArray):
        select = min(range(i, len(ptrArray)), key=ptrArray.__getitem__)
        ptrArray[i], ptrArray[select] = ptrArray[select], val
    return time() - start

#Method 4
#Merge Sort
def mergeSort(ptrArray):
    def recMs(arr):
        count = len(arr)
        if (count > 2):
            left = recMs(arr[:count // 2])
            right = recMs(arr[count // 2:])
            arr = left + right

            last_i = len(arr) - 1
            for i in range(last_i):
                min_val = arr[i]
                min_i = i
                for j in range(i + 1, last_i + 1):
                    if min_val > arr[j]:
                        min_val = arr[j]
                        min_i = j
                if (min_i != i):
                    arr[i], arr[min_i] = arr[min_i], arr[i]
        elif (count == 2 and arr[0] > arr[1]):
            arr[0], arr[1] = arr[1], arr[0]

        return arr

    start = time()
    tmp = recMs(ptrArray)
    stop = time()

    for i in range(len(tmp)):
        ptrArray[i] = tmp[i]
    return stop - start

#Method 5
#Shell's Sort
def shellSort(ptrArray):
    start = time()
    last = len(ptrArray)
    step = last // 2
    while (step > 0):
        for i in range(step, last):
            tmp = ptrArray[i]
            j = i
            while (j >= step and ptrArray[j - step] > tmp):
                ptrArray[j] = ptrArray[j - step]
                j -= step
            ptrArray[j] = tmp
        step //= 2
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
            if (p - low < high - p):
                recQs(arr, low, p)
                low = p + 1
            else:
                recQs(arr, p + 1, high)
                high = p

    start = time()
    recQs(ptrArray, 0, len(ptrArray) - 1)
    return time() - start

