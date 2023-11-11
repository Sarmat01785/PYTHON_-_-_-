# Выражение генератор
"""
Выражение-генератор в Python - это компактный способ создания последовательностей элементов. 
Оно позволяет генерировать значения "на лету" без необходимости создавать полный список. Это особенно полезно, 
когда нужно обработать большие объемы данных или когда список может быть бесконечным.

Выражение-генератор создается с использованием круглых скобок и выглядит как обычное выражение, 
но вместо списка значений оно возвращает объект-генератор, который можно использовать для итерации по значениям. 
Выражение-генератор состоит из выражения, за которым следует цикл for, определяющий значения, которые нужно генерировать.
"""
# Вот пример выражения-генератора, которое генерирует квадраты чисел от 1 до 5:
squares = (x**2 for x in range(1, 6))

for square in squares:
    # print(square)
    print(*squares, sep=" ")

"""
В этом примере переменная squares будет представлять собой объект-генератор, 
который будет генерировать квадраты чисел от 1 до 5. Чтобы получить фактические значения, 
мы можем использовать цикл for или функцию next():
"""
# Можно также использовать выражение-генератор для фильтрации значений или применения функции к каждому элементу.
# Например, следующий пример генерирует только четные числа, возводит их в куб и выводит результаты:
cubes = (x**3 for x in range(1, 11) if x % 2 == 0)

for cube in cubes:
    # print(cube)
    print(*cubes, sep=" ")

"""
Выражения-генераторы могут быть очень полезными инструментами для работы с данными в Python, 
особенно когда нужно обрабатывать большие объемы данных или работать с бесконечными последовательностями.
"""


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]

# n = [x.split('\\')[1] for x in h]  # Генератор списка
# print(n) # ['www.сайт.com', 'www.какойтосайт.net', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтишка.net', 'www.сайтец.com']


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]

# n = [x.split('\\')[1] for x in h if '.com' in x]  # Генератор списка
# print(n) # ['www.сайт.com', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтец.com']


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]

# n = [x.split('\\')[1] for x in h if '.com' in x]  # Генератор списка
# print(n) # ['www.сайт.com', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтец.com']
# print(type(n)) # <class 'list'>


# z = (x.split('\\')[1] for x in h if '.com' in x)  # Выражение генератор
# print(z) # <generator object <genexpr> at 0x0000024EF40A6420>
# print(type(z)) # <class 'generator'>


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]

# # n = [x.split('\\')[1] for x in h if '.com' in x]  # Генератор списка
# # print(n) # ['www.сайт.com', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтец.com']
# # print(type(n)) # <class 'list'>


# z = (x.split('\\')[1] for x in h if '.com' in x)  # Выражение генератор

# for i in z:
#     print(i)
#     # print(*i, sep=" ")


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]

# n = [x.split('\\')[1] for x in h if '.com' in x]  # Генератор списка
# print(n) # ['www.сайт.com', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтец.com']
# print(type(n)) # <class 'list'>
# print(n[0]) # www.сайт.com


# z = (x.split('\\')[1] for x in h if '.com' in x)  # Выражение генератор

# print(z) # <generator object <genexpr> at 0x000002B1E1096420>
# print(type(z)) # <class 'generator'>
# print(next(z)) # www.сайт.com
# print(next(z)) # www.левыйсайт.com
# print(next(z)) # www.другойсайт.com
# print(next(z)) # www.сайтец.com
# print(next(z)) # StopIteration
# print(next(z)) #


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]

# z = (x.split("\\")[1] for x in h if ".com" in x)  # Выражение генератор
# print(next(z))  # www.сайт.com
# print(next(z))  # www.левыйсайт.com
# print(next(z))  # www.другойсайт.com
# print(next(z))  # www.сайтец.com


# h = [
#     "https:\\www.сайт.com",
#     "https:\\www.какойтосайт.net",
#     "https:\\www.левыйсайт.com",
#     "https:\\www.другойсайт.com",
#     "https:\\www.сайтишка.net",
#     "https:\\www.сайтец.com",
# ]


# z = (x.split("\\")[1] for x in h if ".com" in x)  # Выражение генератор

# z_list = list(z)  # Преобразуем генератор в список
# print(z_list)  # ['www.сайт.com', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтец.com']
# print(type(z_list))  # <class 'list'>
# print(z_list[1])  # www.левыйсайт.com


import os


n = [x for x in os.walk("C:\\")]  # Генератор списка

print("Здесь")
print(len(n))
print(n.__sizeof__())

z = (y for y in os.walk("C:\\"))  # Выражение генератор

print("Тут")
print(z.__sizeof__())
print(next(z))
