# Строки и методы форматирования строк в Python

# Пример использования f-строки для подстановки значения переменных в строку
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Выводит: My name is Alice and I am 25 years old.

# F-строки также позволяют выполнять вычисления и вызовы функций
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}.")
# Выводит: The sum of 10 and 5 is 15.

# Форматирование с использованием f-строк
pi = 3.141592653589793
print(f"Pi with 2 decimal places: {pi:.2f}")
# Выводит: Pi with 2 decimal places: 3.14
print(f"Pi with 10 characters, aligned to the right: {pi:>10.2f}")
# Выводит: Pi with 10 characters, aligned to the right:       3.14

# Использование старых методов форматирования: %s и .format()
# Старый стиль с использованием %s
enter = input('Your name: ')
s = 'Hello %s' % enter
print(s)
# Выводит: Hello [введенное имя]

# Стиль format()
s = "Hello {} I am {}".format(enter, "Python")
print(s)
# Выводит: Hello [введенное имя] I am Python

# Можно использовать индексы для указания порядка аргументов
s = "Hello {1} I am {0}".format("Python", enter)
print(s)
# Выводит: Hello [введенное имя] I am Python

# Пример использования f-строки с выражениями и функциями
s = f"Hello {enter}, I can do it in f-string {2 + 2}"
print(s)
# Выводит: Hello [введенное имя], I can do it in f-string 4

# Пример использования функции len() в f-строке
var = 'stroka'
s = f"Hello {enter}, I can do it in f-string {len(var)}"
print(s)
# Выводит: Hello [введенное имя], I can do it in f-string 6
