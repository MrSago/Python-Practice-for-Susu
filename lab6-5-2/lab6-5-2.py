
from my_module import fileListCurDir, listPrint, outRes

if __name__ == "__main__":
    print("Лабораторная работа lab6-5-2")
    print("Вариант №2")
    print("Всё о цифрах в числе\n")

    fInput = "input.txt"
    fOutput = "output.txt"
    fList = fileListCurDir()

    print("Кол-во файлов и папок в текущей директории: %d" % len(fList))
    listPrint(fList)

    outRes(fList, fInput, fOutput)

