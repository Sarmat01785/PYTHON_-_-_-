# Цикл for, цикл в цикле и функция range.

"""
Цикл for используется для итерации по элементам последовательности.
Функция range генерирует последовательность чисел, что делает ее идеальной для использования с циклом for.
"""

# Пример использования цикла for с функцией range:
for i in range(5):
    print(i)  # Выведет числа от 0 до 4

"""
Вложенные циклы используются для выполнения операций для каждой комбинации элементов двух последовательностей.
"""
# Пример вложенных циклов:
for i in range(3):
    for j in range(2):
        print(i, j)  # Выведет комбинации (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)

"""
Функция range может принимать от одного до трех аргументов:
- range(stop): генерирует числа от 0 до stop-1
- range(start, stop): генерирует числа от start до stop-1
- range(start, stop, step): генерирует числа от start до stop-1 с интервалом step
"""
# Примеры использования функции range с разными параметрами:
for i in range(10):
    print(i)  # Числа от 0 до 9

for i in range(5, 10):
    print(i)  # Числа от 5 до 9

for i in range(1, 10, 2):
    print(i)  # Нечетные числа от 1 до 9

for i in range(10, -10, -2):
    print(i)  # Числа от 10 до -8, уменьшающиеся на 2

# Подсчет количества каждой буквы в пользовательском вводе:
alphabet = "абвгдеёжзиклмнопрстуфхцчшщьыъэюя"
user_input = input("Введите строку:\n ")  # Запрашиваем у пользователя строку
for letter in alphabet:
    count = user_input.count(letter)  # Используем метод count для подсчета букв
    if count > 0:
        print(f"Букв {letter} было {count}")
