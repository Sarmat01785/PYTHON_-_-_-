# Функции с переменным количеством аргументов в Python
"""
В Python функции могут быть определены так, чтобы принимать переменное количество аргументов.
Это достигается с помощью параметра *args.
"""

"""
Использование *args

Параметр *args позволяет функции принимать любое количество позиционных аргументов в виде кортежа.
Внутри функции аргументы, переданные через *args, доступны как кортеж.
"""


# Пример функции с *args

def print_arguments(*args):
    for arg in args:
        print(arg)


print_arguments('Hello', 'world', '!')
"""
Вызов print_arguments('Hello', 'world', '!') выведет:
Hello
world
!
"""


"""
Передача аргументов другой функции

Функции, принимающие *args, могут передавать эти аргументы другим функциям.
"""


# Примеры функций для сложения и умножения

def add_numbers(*args):
    return sum(args)


def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result


numbers = (2, 4, 6)
print(add_numbers(*numbers))  # Вывод: 12
print(multiply_numbers(*numbers))  # Вывод: 48

"""
Объединение уникальных элементов из нескольких списков
Можно использовать *args для создания функции, которая объединяет уникальные элементы из нескольких списков.
"""


# Функция для объединения уникальных элементов

def exclusive_item(*args):
    unique_items = set()
    for sequence in args:
        unique_items.update(sequence)
    return list(unique_items)


# Пример использования
z = [9, 8, 7]
x = [8, 8, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

print(exclusive_item(z, x, c))  # Вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Сортировка результата
Функция может также принимать ключевой аргумент для опции сортировки результата.
"""


# Функция с опцией сортировки

def exclusive_item(*args, key=False):
    unique_items = set()
    for sequence in args:
        unique_items.update(sequence)
    result = list(unique_items)
    if key:
        result.sort()
    return result


# Пример использования с ключом сортировки
print(exclusive_item(z, x, c, key=True))  # Выведет отсортированный список

"""
Использование вместе с другими параметрами

 *args можно комбинировать с обычными позиционными параметрами и ключевыми параметрами.
"""


# Пример комбинированного использования

def greet(name, *args):
    print(f"Hello, {name}!")
    for arg in args:
        print(f"Also hello to {arg}")


greet("Alice", "Bob", "Charlie")  # Приветствует Alice, а затем каждого из args
