
def recursiveFunction(n, x, dict):
    if (n in dict.keys()):
        return (dict[n])

    res = ((2*n-1) * x * recursiveFunction(n-1, x, dict) - (n-1) * recursiveFunction(n-2, x, dict)) / n

    dict[n] = res
    return (res)

def P(n, x):
    strRes = ""
    dict = {0: 1, 1: x}

    recursiveFunction(n, x, dict)

    for i in range(0, n + 11):
        number = round(dict[i], 3)
        if (int(number) == float(number)):
            number = int(number)
        else:
            number = float(number)
        strRes += str(number) + " "

    return (strRes)


if __name__ == "__main__":
    n, x = input().split()
    n = int(n)
    x = float(x)
    with open("output.txt", "w") as f:
        f.write(P(n,x))

