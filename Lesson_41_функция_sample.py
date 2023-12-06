# Тема урока: функция sample()
"""
Функция sample() в Python используется для выборки случайных элементов из заданного итерируемого объекта.
Она очень полезна, когда вам нужно получить несколько случайных элементов из списка или кортежа.
"""
# Пример:
import random

# Пример 1: Выборка случайного элемента из списка
my_list = [1, 2, 3, 4, 5]
random_element = random.sample(my_list, 1)
print(random_element)

# Пример 2: Выборка нескольких случайных элементов из списка
random_elements = random.sample(my_list, 3)
print(random_elements)

# Пример 3: Выборка случайного элемента из строки
my_string = "Hello, World!"
random_character = random.sample(my_string, 1)
print(random_character)
