# Списки, тип данных list
"""
Список - это изменяемый упорядоченный тип данных, который может содержать элементы разных типов.
"""

# Создание списка чисел
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Выводит [1, 2, 3, 4, 5]

# Создание списка с элементами разных типов
mixed_list = [1, "hello", True, 3.14]
print(mixed_list)  # Выводит [1, "hello", True, 3.14]

# Доступ к элементам списка по индексу
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Выводит "apple"
print(fruits[1])  # Выводит "banana"
print(fruits[2])  # Выводит "cherry"

# Изменение элементов списка
fruits[0] = "kiwi"  # Заменяем "apple" на "kiwi"
print(fruits)  # Выводит ["kiwi", "banana", "cherry"]

# Работа с отрицательной индексацией
print(fruits[-1])  # Выводит последний элемент списка "cherry"

# Вложенные списки
nested_list = [1, 2, ["apple", "banana"], ["cherry", "kiwi"]]
print(nested_list[2][0])  # Выводит "apple"

# Конкатенация и умножение списков
numbers = [1, 2, 3]
numbers = numbers + [4, 5]  # Добавление элементов в список
print(numbers)  # Выводит [1, 2, 3, 4, 5]

# Создание списка с использованием функции range
range_list = list(range(10))
print(range_list)  # Выводит список чисел от 0 до 9

# Итерация по списку с использованием цикла for
for number in range_list:
    print(number)  # Печатает каждый элемент списка

# Операции с элементами списка в цикле
filtered_list = []
for number in range_list:
    if number == 8:
        continue  # Пропускаем число 8
    filtered_list.append(number)  # Добавляем элемент в новый список
print(filtered_list)  # Выводит список без числа 8
