#  Тема урока: функция split(), map(), apply(), zip().

""""
1. Функция split():
Функция split() разделяет строку на подстроки, используя разделитель,
и возвращает список этих подстрок. Разделитель может быть пробелом, запятой или любым другим символом.
"""
# Пример:
sentence = "Привет, как дела?"
words = sentence.split(", ")
print(words)  # ['Привет', 'как дела?']

"""
2. Функция map():
Функция map() применяет заданную функцию к каждому элементу последовательности 
и возвращает новую последовательность с результатами.
"""
# Пример:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

"""
3. Функция apply():
Функция apply() применяет заданную функцию к каждому элементу объекта 
pandas DataFrame или Series и возвращает новый объект с результатами.
"""
# Пример:
import pandas as pd

data = {'Name': ['John', 'Emily', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)


def add_5(x):
    return x + 5


df['Age'] = df['Age'].apply(add_5)
print(df)
# Name  Age
# 0    John   30
# 1   Emily   35
# 2  Charlie   40


"""
4. Функция zip():
Функция zip() объединяет элементы из нескольких последовательностей в кортежи и 
возвращает итератор, который генерирует эти кортежи.
"""
# Пример:
names = ['John', 'Emily', 'Charlie']
ages = [25, 30, 35]
pairs = list(zip(names, ages))
print(pairs)  # [('John', 25), ('Emily', 30), ('Charlie', 35)]
