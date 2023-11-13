# f-строка, форматирование строк
# %s, .format, f - строка
'''
F-строки представляют способ форматирования строк, который был добавлен в Python 3.6.
Они позволяют встраивать значения переменных и выражений внутри строк, 
обрамляя их символом "f" перед началом строки.
'''

# пример, как использовать f-строки для подстановки значения переменной в строку:
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
'''
В этом примере мы используем фигурные скобки {} для указания места, 
где нужно подставить значения переменных name и age. 
При выполнении программы значения этих переменных будут 
подставлены в соответствующие места в строке.
'''


# Кроме того, f-строки позволяют выполнять выражения и 
# вызывать методы прямо внутри строки. 
# пример:
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}.") # The sum of 10 and 5 is 15.
'''
В этом примере мы выполняем сложение переменных x и y прямо внутри строки, используя выражение {x + y}.
'''


# Также можно использовать форматирование для отображения чисел с определенным 
# количеством знаков после запятой или для указания ширины поля. 
# Вот несколько примеров:
pi = 3.141592653589793
print(f"Pi with 2 decimal places: {pi:.2f}") # Pi with 2 decimal places: 3.14
print(f"Pi with 10 characters, aligned to the right: {pi:>10}") # Pi with 2 decimal places: 3.14
'''
В первом примере мы указываем, что хотим вывести число pi с 
двумя знаками после запятой, используя форматирование :.2f. 

Во втором примере мы указываем, что хотим вывести число pi в 
поле шириной 10 символов, выравненное по правому краю, используя форматирование :>10.
'''






# enter= input('Your name: ')

# s = 'Hello %s' % enter

# print(s)


# enter = input("Your name: ")

# s = "Hello %s I am %s" % (enter, "Python")

# print(s)

# enter = input("Your name: ")
# s = "Hello {} I am {}".format(enter, "Python")
# print(s)


# enter = input("Your name: ")
# s = "Hello {1} I am {0}".format(enter, "Python")
# print(s)

# enter = input("Your name: ") # Alex
# s = f"Hello {enter}, I can do it in f-string {2 + 2}"
# print(s) # Hello Alex, I can do it in f-string 4


# enter = input("Your name: ") # Alex
# var = 'stroka'
# s = f"Hello {enter}, I can do it in f-string {len(var)}"
# print(s) # Hello Alex, I can do it in f-string 6