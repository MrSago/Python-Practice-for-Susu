
from my_module import getInputFromFile, PrintRectangle, PrintSquare


if __name__ == "__main__":
    print("Лабораторная работа lab6-5-1")
    print("Вариант №1")
    print("Прямоугольники и квадраты\n")

    fInput = "input.txt"
    input = getInputFromFile(fInput)

    if (len(input) == 3):
        PrintRectangle(input[0], input[1], input[2])
        print("Прямоугольник из символов \'*\' со сторонами %s и %s сохранен в файл: \"%s\"" % (input[0], input[1], input[2]))
    elif (len(input) == 2):
        PrintSquare(input[0], input[1])
        print("Квадрат из символов \'*\' со стороной %s сохранен в файл: \"%s\"" % (input[0], input[1]))
    else:
        print("Недостаточно аргументов!")
