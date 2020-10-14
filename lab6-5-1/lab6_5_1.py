
from my_module import getInput, PrintRectangle, PrintSquare

if __name__ == "__main__":
    input = getInput()
    if (len(input) == 3):
        PrintRectangle(input[0], input[1], input[2])
    elif (len(input) == 2):
        PrintSquare(input[0], input[1])
    else:
        print("Недостаточно аргументов!")
