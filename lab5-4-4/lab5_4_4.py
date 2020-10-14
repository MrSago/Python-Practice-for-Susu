
print("Variant #4")
print("Введите сумму покупки в копейках:")

try:
    sum = int(input())
except ValueError:
    print("Значение не является числом!")
    exit(0)

if (sum < 1 or sum > 100000):
    print("Число выходит из диапазона: [1;100000]")
    exit(0)


Rub = sum // 100
Kop = sum % 100

def iDigit(num, i):
    strNum = str(num)
    strLen = len(strNum)
    if (strLen < i):
        return (0)
    else:
        return (int(strNum[strLen - i]))

fRubDigit = iDigit(Rub, 1)
sRubDigit = iDigit(Rub, 2)

fKopDigit = iDigit(Kop, 1)
sKopDigit = iDigit(Kop, 2)

strRub = ""
strKop = ""

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

print("%d %s" % (Rub, strRub))
print("%d %s" % (Kop, strKop))
