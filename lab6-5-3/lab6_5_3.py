
from my_module import fileListCurDir, listPrint, outFunc


if __name__ == "__main__":
    fInput = "input.txt"
    fList = fileListCurDir()

    print("Кол-во файлов и папок в текущей директории: %d" % len(fList))
    listPrint(fList)

    if (fInput in fList):
        print("%s присутствует в текущей директории!" % fInput)
        check = True
    else:
        print("%s отсутствует в текущей директории!" % fInput)
        check = False

    outFunc(fInput, check)
