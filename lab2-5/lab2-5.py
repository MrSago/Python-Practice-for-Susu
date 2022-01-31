
# Переменные булева типа могут принимать только два значения.
# С помощью оператора сравнения == выведите два возможных значения переменной is_equal.
# Обратите внимание на результат применения функции int() к булевому значению.


two = 2

three = 3

#

is_equal = two == three

print(int(is_equal))
print(str(is_equal))
print('')

#

is_greater = three > two
print(int(is_greater))
print(str(is_greater))
print('')


##

is_greater = not three < two
print(int(is_greater))
print(str(is_greater))
print('')

##

"""
В языке Python поддерживается множество операций сравнения( ==, >=, < и т.д.).
Все подобные операции имеют одинаковый приоритет. Результат сравнения - булева переменная.
Сравнения могут осуществляться в любом порядке.
"""


one = 1

two = 2

three = 3

print(one < two < three)  # Сравнения (one < two) и (two < three) происходят в одно и то же время.
print('')

# Создайте несколько переменных и осуществите различные сравнения между ними, выведите результаты в консоль.

var1 = 15.23
var2 = 15.21132
var3 = 232

print(var1 > var2)
print(var1 < var2 < var3)

