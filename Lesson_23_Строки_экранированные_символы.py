# Строки, экранированные символы
'''
Строки в языке программирования Python используются для хранения текстовых данных. 
Когда в строке требуется использовать специальные символы, такие как кавычки или перенос строки, 
нужно использовать экранированные символы. Экранированный символ обозначается 
обратной косой чертой (\\) перед особым символом.
'''

# Вот несколько примеров экранированных символов:

# 1. Экранирование кавычек:
string_with_quotes = "I\'m a string with quotes"
print(string_with_quotes) # I'm a string with quotes


# 2. Экранирование обратной косой черты:
string_with_backslash = "This is a backslash: \\"
print(string_with_backslash) # This is a backslash: \


# 3. Экранирование переноса строки:
multi_line_string = "This is a multi-line string.\nHere is the second line."
print(multi_line_string) # This is a multi-line string.
                         # Here is the second line.


# 4. Экранирование символа табуляции:
tabbed_string = "This is a tabbed string.\tHere is some tabbed text."
print(tabbed_string) # This is a tabbed string.    Here is some tabbed text.









# s = "Lets write a string as 's'"

# print(s) # Lets write a string as 's'


# s = 'Let\'s write a string as "s"'

# print(s) # Let's write a string as "s"


# s = "Lets \
#     write a \
#         string as s"
# print(s) # Lets     write a         string as s


# s = "Lets write\ a string as s"

# print(s)  # Lets write\ a string as s


# s = 'Lets write a stri\ng as s'

# print(s)  # Lets write a stri
#           # g as s


# s = 'Lets write a stri\nng as s'

# print(s)  # Lets write a stri
#           # ng as s


# s = 'Let\'s write a string as s'

# print(s)  # Let's write a string as s


# s = "Let's write a string as s"

# url = "https:\\www.youtube.com"

# print(url)  # https:\www.youtube.com


# s = "Let's write a string as s"

# url = "https:\\www.youtube.com\\new"

# print(url)  # https:\www.youtube.com\new


# import os
# s = "Let's write a string as s"

# url = r"https:\\www.youtube.com\new"

# # os.walk("D:\\")

# print(url)  # https:\www.youtube.com\new


# s = "Let's write a string as s"

# url = "https:\\www.youtube.com\\new"

# x = 'C:\\Users\\PyHS\\Desktop'

# print(x) # C:\Users\PyHS\Desktop
# print(url)  # https:\www.youtube.com\new
