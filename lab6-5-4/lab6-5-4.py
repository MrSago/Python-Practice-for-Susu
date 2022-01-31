
from my_module import fileListCurDir, listPrint, outRes

if __name__ == "__main__":
    print("Лабораторная работа lab6-5-4")
    print("Вариант №4")
    print("Особые точки\n")

    fInput = "input.txt"
    fOutput = "output.txt"
    fList = fileListCurDir()

    print("Кол-во файлов и папок в текущей директории: %d" % len(fList))
    listPrint(fList)

    outRes(fList, fInput, fOutput)

