# Кортежи, тип данных tuple

"""
Кортежи (tuple) - это неизменяемые коллекции в Python, используемые для хранения упорядоченных элементов.
"""

# Создание кортежей
coordinates = (10, 20)
fruits = "apple", "banana", "orange"
single_value_tuple = (42,)

# Доступ к элементам кортежа
print(coordinates[0])  # Выведет: 10
print(fruits[1])  # Выведет: banana

# Создание нового кортежа из существующего
extended_coordinates = coordinates + (30, 40)
print(extended_coordinates)  # Выведет: (10, 20, 30, 40)

# Распаковка кортежа
x, y = coordinates
print(x)  # Выведет: 10
print(y)  # Выведет: 20

# Методы кортежа
# count() - подсчитывает количество вхождений элемента
# index() - возвращает индекс первого вхождения элемента
test_tuple = (9, 8, 7, 9, 6, 5, 9, 4, 3)
print(test_tuple.count(9))  # Выведет: 3
print(test_tuple.index(9))  # Выведет: 0

# Добавление кортежей
numbers_tuple = (1, 2, 3)
numbers_tuple += (4, 5)
print(numbers_tuple)  # Выведет: (1, 2, 3, 4, 5)

# Копирование кортежа
original_tuple = numbers_tuple
numbers_tuple += (6, 7)
print(original_tuple)  # Выведет: (1, 2, 3, 4, 5)
print(numbers_tuple)  # Выведет: (1, 2, 3, 4, 5, 6, 7)

# Неизменяемость кортежей
# Следующий код вызовет ошибку, потому что кортежи не поддерживают изменение элементов
numbers_tuple[0] = 10
print(numbers_tuple[0])  # TypeError: 'tuple' object does not support item assignment
