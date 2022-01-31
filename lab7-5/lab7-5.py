
def countNum(listInput):
    if (len(listInput)):
        if (listInput.pop().isdigit()):
            return (1 + countNum(listInput))
        return (countNum(listInput))
    return (0)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        listInput = [str(i) for i in f.readline()]
    print(countNum(listInput))

