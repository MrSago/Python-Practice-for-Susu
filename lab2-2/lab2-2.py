
# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9 
print(type(number))   # Вывод типа переменной number 


# Создайте ещё несколько переменных разных типов и осуществите вывод их типов

float_number = 9.5 
print(type(float_number))

str_type = "3232"
print(type(str_type))

bool_type = True
print(type(bool_type))

list_type = [ "qwer", "asd", 545 ]
print(type(list_type))

dict_type = { 1:23, 2:54 }
print(type(dict_type))

cortezh_type = ( 2, 6 )
print(type(cortezh_type))


# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

print(int(str_type))
print(int(float_number))
print(float(str_type))
print("float_number = " + str(float_number))

