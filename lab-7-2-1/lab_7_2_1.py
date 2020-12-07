from sys import setrecursionlimit

M = N = 0
result = []
setrecursionlimit(10**5)

def isSolve():
    global result
    for i in result:
        if (i == 0):
            return False
    return True

def isValid(x, y):
    global M, N
    global result
    if (1 <= x <= M and 1 <= y <= N and result[-y][x-1] == 0):
        return True
    return False

def paths(x, y, variant):
    variation = {
        0: (x+2, y+1),
        1: (x+2, y-1),
        2: (x-2, y+1),
        3: (x-2, y-1),
        4: (x+1, y+2),
        5: (x+1, y-2),
        6: (x-1, y+2),
        7: (x-1, y-2),
    }
    return variation[variant]

def output(M, N):
    global result
    for i in range(M):
        for j in result[i]:
            print(f"{j:{len(str(N*M))}}", end=' ')
        print("")

def AllowPath(x, y, step=1):
    global result
    result[-y][x-1] = step

    OpenWays = []
    for openway in range(8):
        NewX, NewY = paths(x, y, openway)
        if isValid(NewX, NewY):
            OpenWays.append((NewX, NewY))

    LensWays = {}
    for waylens in OpenWays:
        count = 0
        for openway in range(8):
            TempX, TempY = waylens
            NewX, NewY = paths(TempX, TempY, openway)
            if isValid(NewX, NewY):
                count += 1
        LensWays[count] = waylens
    if LensWays:
        x, y = LensWays[min(LensWays)]
        return AllowPath(x, y, step+1)

    return result


def knightTour():
    global M, N
    M, N = map(int, input("Введите размерность (M, N): ").split())
    X, Y = map(int, input("Введите начальные координаты (X, Y): ").split())
    
    if (M*N % 2 != 0 and X+Y % 2 != 0):
        print("Решения нет")
        return

    global result
    result = [[0 for j in range(M)] for i in range(N)]

    AllowPath(X, Y)

    if (not isSolve()):
        print("Решения нет")
        return

    print("\nРезультат обхода:")
    output(M, N)



if __name__ == "__main__":
    print("Лабораторная работа lab-7-2-1")
    print("Задача о ходе коня")
    knightTour()
