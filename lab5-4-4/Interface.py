
from ModuleTest import simpleTest, moduleTest


def startMenu():
    while (True):
        print("\nВыберите действие:")
        print("1. Ввести значения")
        print("2. Пройти модульный тест")
        print("0. Выход из программы")

        select = input()
        if (select == '1'):
            inputSimpleTest()
        elif (select == '2'):
            inputModuleTest()
        elif (select == '0'):
            break
        else:
            print("Нет такого пункта!")

def inputSimpleTest():
    sum = input("Введите сумму покупки в копейках:\n")
    res = simpleTest(sum)
    print(res)

def inputModuleTest():
    print("\nВведите диапазон [a; b] и шаг step:")
    a = input("a = ")
    b = input("b = ")
    step = input("step = ")
    res = moduleTest(a, b, step)
    print(res)
