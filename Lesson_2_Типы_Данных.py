# Типы данных.

# Целые числа
x = 5
y = -10

# Вещественные числа
pi = 3.14
temperature = 25.5

# Строки
message = "Привет, мир!"
name = 'Alice'

# Списки
numbers = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'банан', 'апельсин']

# Кортежи
coordinates = (10, 20)
person = ('John', 25, 'Москва')

# Словари
student = {'имя': 'Alice', 'возраст': 20, 'курс': 'Python'}
country = {'название': 'Россия', 'столица': 'Москва', 'население': 12000000}

# Множества
set1 = {1, 2, 3, 4}
set2 = {'яблоко', 'банан', 'апельсин'}





a = None  # отсутствие данных.
print(type(a))
a = 1  # целое число.
print(type(a))
a = 1.0  # Число с плавающей точкой.
print(type(a))
a = 1 + 1j  # Комплексное число.
print(type(a))
a = "1"  # Строка.
print(type(a))
a = [1, 1, "a"]  # Список.
print(type(a))
a = (1, 1, "a")  # Картеж.
print(type(a))
a = {1, 1, "a"}  # Множества.
print(type(a))
a = {"a": 1, "b": 2}  # Словарь.
print(type(a))
a = True             # Логические bool значения.
print(type(a))
a = False            # Логические bool значения.
print(type(a))



# Ввод


# x = input("Ввод: ")
# print(type(x))

# x = input("Ввод: ")
# r = int(x) + 5
# print(r)
# print(type(r))

# x = input("Ввод: ")
# r = float(x) + 5
# print(r)
# print(type(r))

x = float(input("Введите число: "))
y = float(input("Введите число: "))
r = x + y
print("Результат" + str(r))
