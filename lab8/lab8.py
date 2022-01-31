
import sort
from random import randint
from prettytable import PrettyTable

def initTestArrays(N):
    arr = [[], [], []]
    arr[0] = [int(i) for i in range(1, N + 1, 1)]
    for i in range(0, N): arr[1].append(randint(-1000000000, 1000000000))
    arr[2] = [int(i) for i in range(N, 0, -1)]
    return arr

def copyTestArrays(arr):
    new_arr = [[], [], []]
    new_arr[0] = arr[0].copy()
    new_arr[1] = arr[1].copy()
    new_arr[2] = arr[2].copy()
    return new_arr

def resTestFun(fun, test):
    input = copyTestArrays(test)
    ls = ["%0.8f" % round(fun(input[0]), 8)]
    if (not sort.Check(input[0])):
        raise Exception("input[0] not sorted in function: %s" % fun.__name__)
    ls += ["%0.8f" % round(fun(input[1]), 8)]
    if (not sort.Check(input[1])):
        raise Exception("input[1] not sorted in function: %s" % fun.__name__)
    ls += ["%0.8f" % round(fun(input[2]), 8)]
    if (not sort.Check(input[2])):
        raise Exception("input[2] not sorted in function: %s" % fun.__name__)
    return ls

def startSort():
    N = int(input())
    test_arrays = initTestArrays(N)

    table = PrettyTable()
    table.field_names = ["№", "Метод", "Отсортированная", "Случайная", "В обратом порядке"]

    table.add_row(["0", "Python Sort"] + resTestFun(sort.pySort, test_arrays))
    table.add_row(["1", "Bubble Sort"] + resTestFun(sort.bubbleSort, test_arrays))
    table.add_row(["2", "Insertion Sort"] + resTestFun(sort.insertionSort, test_arrays))
    table.add_row(["3", "Selection Sort"] + resTestFun(sort.selectionSort, test_arrays))
    table.add_row(["4", "Merge Sort"] + resTestFun(sort.mergeSort, test_arrays))
    table.add_row(["5", "Shell's Sort"] + resTestFun(sort.shellSort, test_arrays))
    table.add_row(["6", "Quick Sort"] + resTestFun(sort.quickSort, test_arrays))

    print("Количество элементов: %d" % N)
    print(table)

if __name__ == "__main__":
    startSort()

