# Функции def, параметры и аргументы
'''
Функции в языке программирования Python позволяют объединить повторяющийся 
код в одно место и повторно использовать его при необходимости. 
Они также позволяют передавать значения в функцию в виде аргументов и 
получать результат работы функции в виде возвращаемого значения.

Для создания функции в Python используется ключевое слово def, 
за которым следует имя функции и круглые скобки, в которых указываются параметры 
функции (если они есть). После круглых скобок следует двоеточие, а следующие строки кода, 
отступленные на один уровень, представляют тело функции.
'''
# Вот пример простой функции, которая выводит приветствие на экран:
def say_hello():
    print("Привет, мир!")

say_hello()  # Вызов функции
'''
В данном примере функция say_hello не принимает никаких параметров, поэтому в круглых 
скобках они отсутствуют. При вызове функции say_hello() на экран будет выведено "Привет, мир!".
'''
# Теперь рассмотрим пример функции с параметрами. Предположим, у нас есть функция, 
# которая принимает два числа и возвращает их сумму:
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Выводит 8
'''
В данном примере функция add_numbers принимает два параметра a и b, и возвращает
их сумму с помощью ключевого слова return. При вызове функции add_numbers(3, 5) 
результатом будет число 8, которое затем выводится на экран.
'''


# Также функции могут иметь аргументы по умолчанию. Это позволяет вызывать функцию без 
# указания всех параметров, присваивая им значения по умолчанию. Вот пример:
def calculate_area(length, width=1):
    return length * width

result1 = calculate_area(5)
result2 = calculate_area(5, 3)
print(result1)  # Выводит 5
print(result2)  # Выводит 15
'''
В данном примере функция calculate_area принимает два параметра: length и width, 
где width имеет значение по умолчанию равное 1. При вызове функции calculate_area(5) 
будет вычислена площадь прямоугольника со сторонами 5 и 1, что равно 5. 
При вызове функции calculate_area(5, 3) будет вычислена площадь прямоугольника со сторонами 5 и 3, что равно 15.
'''





# j = [9, 8, 7, 6]
# count = 0
# for i in j:
#     count += 1
# print(count)


# def count_list(parametr):  # parametr - это переменная определенная только в нутри функции
#     count = 0
#     for i in parametr:
#         count += 1
#     return count

# j = [9, 8, 7, 6]
# print(count_list(j))  # Агумент j

# h = ["a", "a", "h"]
# print(count_list(h))

# k = [9, 8, 7, 5, 7, 5]
# print(count_list(k))


# def count_list(parametr):  # parametr - это переменная определенная только в нутри функции
#     count = 0
#     for i in parametr:
#         count += 1
#     return count

# j = [9, 8, 7, 6]
# print(count_list(j))  # Агумент j

# h = ["a", "a", "h"]
# print(count_list(h))

# k = [9, 8, 7, 5, 7, 5]
# print(count_list("string text"))


# def count_list(parametr, count = 0):  # parametr - это переменная определенная только в нутри функции, 
#     # count = 0 - параметр по умолчанию.
    
#     for i in parametr:
#         count += 1
#     return count
# j = [9, 8, 7, 6]
# print(count_list(j))

# def count_list(parametr, count):  # parametr - это переменная определенная только в нутри функции, 
#     # count - параметр по умолчанию.
    
#     for i in parametr:
#         count += 1
#     return count
# j = [9, 8, 7, 6]
# print(count_list(j , 0))

# def count_list(parametr, count):  # parametr - это переменная определенная только в нутри функции.
    # count - параметр по умолчанию.
#     for i in parametr:
#         count += 1
#     return count
# j = [9, 8, 7, 6]
# print(count_list(j , -1))  # Возвращает индекс последнего элемента. 3


# def count_list(parametr, count = 0):  # parametr - это переменная определенная только в нутри функции, 
#     # count = 0 - параметр по умолчанию.
    
#     for i in parametr:
#         count += 1
#     return count
# j = [9, 8, 7, 6]
# print(count_list(j , -1))  # Возвращает индекс последнего элемента. 3

# def count_list(parametr,parametr2 = False, count = 0):  # В этой функции три параметра, один обычный два по умалчанию.
#     if parametr2 == True:
#         typ = type(parametr[0])
#         for i in parametr:
#             count += 1
#         return count, typ
#     else:
        
#         for i in parametr:
#             count += 1
#         return count
# j = [9, 8, 7, 6]
# print(count_list(j))  # Аргумент j




# def count_list(parametr,parametr2 = False, count = 0):
    
#     if parametr2 == True:
#         typ = type(parametr[0])
#         for i in parametr:
#             count += 1
#         return count, typ
#     else:
        
#         for i in parametr:
#             count += 1
#         return count
# j = [9, 8, 7, 6]
# print(count_list(j, count=-1))


# def count_list(parametr,parametr2 = False, count = 0):
    
#     if parametr2 == True:
#         typ = type(parametr[0])
#         for i in parametr:
#             count += 1
#         return count, typ
#     else:
        
#         for i in parametr:
#             count += 1
#         return count
# j = [9, 8, 7, 6]
# print(count_list(j, True))


# def count_list(parametr,parametr2 = False, count = 0):
    
#     if parametr2 == True:
#         typ = type(parametr[0])
#         for i in parametr:
#             count += 1
#         return count, typ
#     else:
        
#         for i in parametr:
#             count += 1
#         return count
# j = [9, 8, 7, 6]
# print(count_list(j, True, -1))  # Можно изменить все три параметра в функции, передав все три аргумента.

