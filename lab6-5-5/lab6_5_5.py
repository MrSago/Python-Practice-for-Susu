
from my_module import fileListCurDir, listPrint, outRes


if __name__ == "__main__":
    print("Лабораторная работа lab6-5-5")
    print("Вариант №4")
    print("Матрицы\n")

    fInput = "input.txt"
    fList = fileListCurDir()

    print("Кол-во файлов и папок в текущей директории: %d" % len(fList))
    listPrint(fList)

    outRes(fList, fInput)
