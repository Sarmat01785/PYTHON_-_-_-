# Lambda-функции в Python

# Lambda-функция - это компактный способ создания анонимных функций, то есть функций без имени.
# Они обычно используются для однократных операций, когда необходима небольшая функция.

# Синтаксис lambda-функции:
# lambda arguments: expression
# Здесь `arguments` - это аргументы, как в обычной функции, а `expression` - выражение,
# значение которого lambda-функция возвращает.

# Примеры использования lambda-функций:

# Сложение двух чисел:
add = lambda x, y: x + y
print(add(5, 3))  # Вывод: 8

# Проверка числа на четность:
is_even = lambda num: num % 2 == 0
print(is_even(4))  # Вывод: True
print(is_even(7))  # Вывод: False

# Использование lambda с map для возведения в квадрат всех чисел списка:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]


# Для сравнения, рассмотрим использование обычной функции и lambda-функции:
def divide_by_five(x):
    return x / 5


lambda_divide_by_five = lambda x: x / 5
print(divide_by_five(7))  # Вывод: 1.4
print(lambda_divide_by_five(7))  # Вывод: 1.4

# Lambda-функции часто используются для указания ключа сортировки:
list_of_people = [["Adam", 29], ["Jonny", 1 / 12], ["Jess", 25]]

# Сортировка списка списков по второму элементу каждого подсписка:
sorted_list = sorted(list_of_people, key=lambda x: x[1])
print(sorted_list)  # Вывод: [['Jonny', 0.08333333333333333], ['Jess', 25], ['Adam', 29]]

# Фильтрация списка с использованием lambda-функции:
adults = list(filter(lambda person: person[1] >= 18, list_of_people))
print(adults)  # Вывод: [['Adam', 29], ['Jess', 25]]

# Lambda-функции являются полезным инструментом для создания коротких функций на лету и часто используются
# там, где функциональность требуется однократно или в небольшом объеме кода.
