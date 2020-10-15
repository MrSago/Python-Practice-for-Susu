
def iDigit(num, i):
    strNum = str(num)
    strLen = len(strNum)
    if (strLen < i):
        return (0)
    else:
        return (int(strNum[strLen - i]))

def fun(sum):
    try:
        sum = int(sum)
    except ValueError:
        return ("Значение не является числом!")

    if (sum < 1 or sum > 100000):
        return ("Число выходит из диапазона: [1;100000]")

    Rub = sum // 100
    Kop = sum % 100

    fRubDigit = iDigit(Rub, 1)
    sRubDigit = iDigit(Rub, 2)

    fKopDigit = iDigit(Kop, 1)
    sKopDigit = iDigit(Kop, 2)

    if (sRubDigit == 1):
        strRub = "РУБЛЕЙ"
    elif (fRubDigit == 1):
        strRub = "РУБЛЬ"
    elif (fRubDigit >= 2 and fRubDigit <= 4):
        strRub = "РУБЛЯ"
    else:
        strRub = "РУБЛЕЙ"

    if (sKopDigit == 1):
        strKop = "КОПЕЕК"
    elif (fKopDigit == 1):
        strKop = "КОПЕЙКА"
    elif (fKopDigit >= 2 and fKopDigit <= 4):
        strKop = "КОПЕЙКИ"
    else:
        strKop = "КОПЕЕК"

    res = ""
    if (Rub != 0):
        res += "%d %s" % (Rub, strRub)
    if (Rub != 0 and Kop != 0):
        res += ' '
    if (Kop != 0):
        res += "%d %s" % (Kop, strKop)
    return (res)
