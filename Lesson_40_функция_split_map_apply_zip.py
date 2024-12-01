# Тема урока: функции split(), map(), apply() и zip().

# 1. Функция split()
# Разделяет строку на список подстрок по указанному разделителю. По умолчанию разделителем является любой пробел.
sentence = "Привет, как дела?"
words = sentence.split(", ")
print(words)  # Вывод: ['Привет', 'как дела?']

# 2. Функция map()
# Применяет функцию ко всем элементам последовательности и возвращает итератор с результатами.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# 3. Метод apply()
# Метод DataFrame или Series в pandas, применяющий функцию к каждому элементу.
import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Emily', 'Charlie'], 'Age': [25, 30, 35]})
df['Age'] = df['Age'].apply(lambda x: x + 5)
print(df)
# Вывод:
#       Name  Age
# 0    John   30
# 1   Emily   35
# 2  Charlie   40

# 4. Функция zip()
# Создает итератор, который агрегирует элементы из нескольких последовательностей в кортежи.
names = ['John', 'Emily', 'Charlie']
ages = [25, 30, 35]
pairs = list(zip(names, ages))
print(pairs)  # Вывод: [('John', 25), ('Emily', 30), ('Charlie', 35)]

# Использование zip() для распаковки последовательности:
first_names, ages = zip(*pairs)
print(first_names)  # Вывод: ('John', 'Emily', 'Charlie')
print(ages)  # Вывод: (25, 30, 35)

# Эти функции упрощают выполнение общих задач программирования, таких как преобразование данных,
# итерация по наборам значений и объединение информации из различных источников.
