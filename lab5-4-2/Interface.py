
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
    try:
        A, B, C = input("\nВведите коэффициенты уравнения Ax^2+Bx+C=0 в виде:\nA B C\n").split()
    except ValueError:
        print("Кол-во коэффициентов должно быть равно трём!")
        return
    res = simpleTest(A, B, C)
    print(res)

def inputModuleTest():
    print("\nВведите диапазон [a; b] и шаг step:")
    a = input("a = ")
    b = input("b = ")
    step = input("step = ")
    res = moduleTest(a, b, step)
    print(res)
