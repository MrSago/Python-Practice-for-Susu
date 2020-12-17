
import sort
from prettytable import PrettyTable
from time import time
from random import randint


def initTestArrays(N):
    arr = [[], [], []]
    arr[0] = [int(i) for i in range(1, N + 1, 1)]
    for i in range(0, N): arr[1].append(randint(-1000000, 1000000))
    arr[2] = [int(i) for i in range(N, 0, -1)]
    return arr

def copyTestArrays(arr):
    new_arr = [[], [], []]
    new_arr[0] = arr[0].copy()
    new_arr[1] = arr[1].copy()
    new_arr[2] = arr[2].copy()
    return new_arr

def startSort():
    N = int(input())
    test_arrays = initTestArrays(N)

    table = PrettyTable()
    table.field_names = ["№", "Метод", "Отсортированная", "Случайная", "В обратом порядке"]

    #Python Sort
    input_arrays = copyTestArrays(test_arrays)
    table.add_row(["0", "Python Sort",
                   "%0.8f" % round(sort.pySort(input_arrays[0]), 8),
                   "%0.8f" % round(sort.pySort(input_arrays[1]), 8),
                   "%0.8f" % round(sort.pySort(input_arrays[2]), 8)])

    #Bubble Sort
    input_arrays = copyTestArrays(test_arrays)
    table.add_row(["1", "Bubble Sort",
                   "%0.8f" % round(sort.bubbleSort(input_arrays[0]), 8),
                   "%0.8f" % round(sort.bubbleSort(input_arrays[1]), 8),
                   "%0.8f" % round(sort.bubbleSort(input_arrays[2]), 8)])

    #Insertion Sort
    input_arrays = copyTestArrays(test_arrays)
    table.add_row(["2", "Insertion Sort",
                   "%0.8f" % round(sort.insertionSort(input_arrays[0]), 8),
                   "%0.8f" % round(sort.insertionSort(input_arrays[1]), 8),
                   "%0.8f" % round(sort.insertionSort(input_arrays[2]), 8)])

    #Quick Sort
    input_arrays = copyTestArrays(test_arrays)
    table.add_row(["6", "Quick Sort",
                   "%0.8f" % round(sort.quickSort(input_arrays[0]), 8),
                   "%0.8f" % round(sort.quickSort(input_arrays[1]), 8),
                   "%0.8f" % round(sort.quickSort(input_arrays[2]), 8)])

    print("Количество элементов: %d" % N)
    print(table)

if __name__ == "__main__":
    startSort()
