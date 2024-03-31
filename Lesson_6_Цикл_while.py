# Цикл while

"""
Цикл while используется для выполнения блока кода до тех пор, пока заданное условие истинно.
"""

# Пример 1: Печать чисел от 1 до 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Рекомендуется использовать оператор += для увеличения i

# Пример 2: Подсчет суммы чисел от 1 до 10
total = 0  # Используем имя переменной 'total', чтобы избежать конфликта с встроенной функцией sum
i = 1
while i <= 10:
    total += i
    i += 1
print("Сумма чисел от 1 до 10:", total)

# Использование else с while
# Цикл while может иметь необязательный блок else. Блок else выполняется, когда условие цикла становится ложным.
x = 0
while x < 5:
    x += 1
else:
    print("Значение x достигло", x)

# Вычисление факториала числа
number = int(input("Введите число: "))
factorial = 1
counter = 1
while counter <= number:
    factorial *= counter
    counter += 1
else:
    print(f"Факториал числа {number} равен {factorial}")

# Бесконечный цикл с вводом данных и выходом по условию
while True:
    entry = input("Введите 'exit' для выхода: ")
    if entry == "exit":
        break  # Выход из цикла

# Пример использования continue и break
input_string = ""
while len(input_string) < 5:
    char = input("Введите символ: ")
    if char == "o":
        continue  # Пропускаем итерацию, если пользователь ввел 'o'
    if char == "l":
        break  # Выходим из цикла, если пользователь ввел 'l'
    input_string += char
else:
    print("Конечная строка:", input_string)
print("Цикл завершен, программа работает дальше.")
