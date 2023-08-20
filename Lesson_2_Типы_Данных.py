# Типы данных.

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
