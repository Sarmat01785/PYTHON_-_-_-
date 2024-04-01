# Функции def, определение и вызов

"""
Функции в Python используются для группировки кода, что облегчает его повторное использование и улучшает читаемость.
"""


# Определение простой функции без аргументов
def greet():
    print("Привет!")


# Вызов функции
greet()


# Определение функции с аргументами
def personalized_greeting(name):
    print(f"Привет, {name}!")


# Вызов функции с передачей аргумента
personalized_greeting("Алексей")


# Определение функции с возвратом значения
def sum_two_numbers(num1, num2):
    return num1 + num2


# Вызов функции и сохранение возвращаемого значения
total = sum_two_numbers(3, 5)
print(total)  # Выводит: 8


# Функции и область видимости
def multiply_by_two(value):
    result = value * 2  # 'result' является локальной переменной внутри функции
    return result


# Вызов функции
multiplication_result = multiply_by_two(5)
print(multiplication_result)  # Выводит: 10

# Глобальные и локальные переменные
global_variable = 10


def function_with_global():
    local_variable = 5
    return local_variable + global_variable


# Вызов функции
print(function_with_global())  # Выведет: 15
