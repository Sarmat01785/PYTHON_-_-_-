# Строки и экранированные символы в Python

# Экранирование кавычек позволяет включать кавычки в строку
string_with_quotes = "I\'m a string with quotes"
print(string_with_quotes)  # Вывод: I'm a string with quotes

# Экранирование обратной косой черты позволяет включить сам символ обратной косой черты в строку
string_with_backslash = "This is a backslash: \\"
print(string_with_backslash)  # Вывод: This is a backslash: \

# Экранирование переноса строки создает многострочный текст в одной строке
multi_line_string = "This is a multi-line string.\nHere is the second line."
print(multi_line_string)
# Вывод:
# This is a multi-line string.
# Here is the second line.

# Экранирование символа табуляции вставляет табуляцию в строку
tabbed_string = "This is a tabbed string.\tHere is some tabbed text."
print(tabbed_string)  # Вывод: This is a tabbed string.    Here is some tabbed text.

# Использование одинарных и двойных кавычек для включения кавычек в строку без экранирования
s = "Let's write a string as 's'"
print(s)  # Вывод: Let's write a string as 's'

s = 'Let\'s write a string as "s"'
print(s)  # Вывод: Let's write a string as "s"

# Raw-строки используются для предотвращения экранирования специальных символов
# Особенно полезны при работе с регулярными выражениями или путями файлов
url = r"https:\\www.youtube.com\new"
print(url)  # Вывод: https:\\www.youtube.com\new

# Пути к файлам в Windows лучше представлять с помощью raw-строк
path = r'C:\Users\PyHS\Desktop'
print(path)  # Вывод: C:\Users\PyHS\Desktop

# URL лучше представлять с использованием прямых слешей
url = "https://www.youtube.com/new"
print(url)  # Вывод: https://www.youtube.com/new
