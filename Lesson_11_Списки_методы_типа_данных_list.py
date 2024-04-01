# Списки, методы типа данных list

"""
Списки в Python - это упорядоченные коллекции элементов, могут содержать разнотипные данные.
Они поддерживают ряд методов для удобной работы с элементами.
"""

# Создание списка и добавление элементов
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]  # Создание пустого списка

# Различные методы работы со списками
print(len(numbers))  # Возвращает количество элементов в списке
print(fruits.index("orange"))  # Возвращает индекс элемента "orange"
print(fruits.count("apple"))  # Возвращает количество элементов "apple" в списке

numbers.sort()  # Сортирует список numbers
print(numbers)

fruits.reverse()  # Меняет порядок элементов в списке fruits на обратный
print(fruits)

fruits.remove("banana")  # Удаляет первое вхождение элемента "banana"
print(fruits)

# Демонстрация правильного удаления элементов в цикле
numbers = list(range(1, 21))
even_numbers = []
odd_numbers = numbers.copy()  # Создание копии списка numbers

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        odd_numbers.remove(number)

print("Нечетные числа:", odd_numbers)
print("Четные числа:", even_numbers)

# Демонстрация срезов списка
slice_example = list(range(1, 21))
every_fifth = slice_example[::5]  # Получаем каждый пятый элемент списка
print("Каждый пятый элемент:", every_fifth)

# Пример использования среза для получения всех элементов после пятого
after_fifth = slice_example[5:]
print("Элементы списка после пятого:", after_fifth)
