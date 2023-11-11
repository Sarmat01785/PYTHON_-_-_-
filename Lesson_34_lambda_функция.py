#  lambda функция
"""
Lambda-функция в Python - это анонимная (безымянная) функция, которая может быть определена 
без использования ключевого слова def. Она используется для создания простых функций, 
которые могут быть переданы в качестве аргументов или возвращены из других функций.
"""
# Простой синтаксис lambda-функции:
# lambda arguments: expression
# Где arguments - список аргументов функции,
# а expression - выражение, которое будет выполнено и возвращено.


# 1. Пример использования lambda-функции для сложения двух чисел:
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Вывод: 8


# 2. Пример использования lambda-функции для проверки, является ли число четным:
is_even = lambda num: num % 2 == 0
print(is_even(4))  # Вывод: True
print(is_even(7))  # Вывод: False


# 3. Пример использования lambda-функции вместе с функцией map() для применения функции к каждому элементу списка:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]


# def some(x):
#     return x/5

# var = lambda x: x/5

# print(some(7)) # 1.4
# print(var(7)) # 1.4


# from dis import dis


# def some(x):
#     return x / 5


# var = lambda x: x / 5
# print(dis(some))
# print(dis(var))


# list_of = [["Adam", 29], ["Jonny", 1 * 1 / 12], ['Jess', 25]]

# def s(x):
#     return x[1]

# r = sorted(list_of, key=s)
# print(r) # [['Jonny', 0.08333333333333333], ['Jess', 25], ['Adam', 29]]


# list_of = [["Adam", 29], ["Jonny", 1 * 1 / 12], ["Jess", 25]]


# r = sorted(list_of, key=lambda x: x[1])
# print(r) # [['Jonny', 0.08333333333333333], ['Jess', 25], ['Adam', 29]]


list_of = [["Adam", 29], ["Jonny", 1 * 1 / 12], ["Jess", 25]]

x = list(filter(lambda x: x[1] > 18, list_of))

print(x) # [['Adam', 29], ['Jess', 25]]
