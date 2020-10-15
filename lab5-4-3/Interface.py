
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
    print("Введите время отправления поезда и время в пути в формате:")
    print("Hotp - время отправления (часы)")
    print("Motp - время отправления (минуты)")
    print("Hp - время в пути (часы)")
    print("Mp - время в пути (минуты)")
    Hotp = input()
    Motp = input()
    Hp = input()
    Mp = input()
    res = simpleTest(Hotp, Motp, Hp, Mp)
    print(res)

def inputModuleTest():
    res = moduleTest()
    print(res)
