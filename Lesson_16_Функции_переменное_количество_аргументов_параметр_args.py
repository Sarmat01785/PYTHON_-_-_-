# Функции переменное количество аргументов, параметр *args
'''
Функции с переменным количеством аргументов позволяют передавать произвольное 
количество аргументов в функцию. В Python для этого используется параметр *args.

Когда вы определяете функцию и указываете *args в качестве параметра, это означает, 
что функция может принимать любое количество аргументов (включая ноль) 
и они будут доступны внутри функции в виде кортежа.
'''
# пример:
def print_arguments(*args):
    for arg in args:
        print(arg)

print_arguments('Hello', 'world', '!')
'''
В этом примере функция print_arguments принимает произвольное количество аргументов, 
используя параметр *args. Затем она перебирает все переданные аргументы и выводит их на экран.
В результате выполнения этого кода будет выведено:
Hello
world
! 
'''


# Еще одна полезная возможность использования *args - передача аргументов другой функции. 
# Рассмотрим следующий пример:
def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

numbers = (2, 4, 6)
sum_result = add_numbers(*numbers)
product_result = multiply_numbers(*numbers)

print(sum_result)  # Output: 12
print(product_result)  # Output: 48
'''
Здесь мы определяем две функции: add_numbers и multiply_numbers, 
обе принимают произвольное количество аргументов. 
Затем мы создаем кортеж numbers и передаем его в качестве аргументов в обе функции, используя оператор *. 
После этого мы выводим результаты сложения и умножения аргументов на экран.
'''









# def name(a):
#     print(a) # 7
# name(7)


# def name(*a):
#     print(a) # (7, 9, 8, 7)
# name(7, 9, 8, 7)


# def name(*args):
#     print(args) # () пустой картеж
# name()

# def name(h, *args):
#     print(h)    # 1
#     print(args) # (2, 3)
# name(1, 2, 3)

# def name(h, g, *args):
#     print(h)    # 1
#     print(g)    # 2
#     print(args) # (3,)
# name(1, 2, 3)


# def name(h=1, g=5, *args):
#     print(h)    # 1
#     print(g)    # 2
#     print(args) # (3,)
# name(1, 2, 3)

# def name(h=1, g=5, *args, key): # Ключивые параметры записываются после *args
#     print(h)    # 1
#     print(g)    # 2
#     print(args) # (3, 5, 6)
#     print(key)  # 10
# name(1, 2, 3, 5, 6, key=10)


# def exclusiv_item(*args):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
            
        
#     return new_list

# z = [9, 8, 7]
# x =[8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]

# t = exclusiv_item(z, x, c)
# print(t)  # [9, 8, 7, 6, 5, 1, 2, 3, 4]



# def exclusiv_item(*args):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
            
        
#     return new_list

# z = [9, 8, 7]
# x =[8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]

# t = exclusiv_item(z, x)
# print(t)  # [9, 8, 7, 6, 5]


# def exclusiv_item(*args):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
            
        
#     return new_list

# z = [9, 8, 7]
# x =[8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]

# t = exclusiv_item()
# print(t)  # [] пустой список


# def exclusiv_item(*args, key=False):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
#     if key == True:
#         new_list.sort
        
            
        
#     return new_list

# z = [9, 8, 7]
# x =[8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]

# t = exclusiv_item(z, x, c, key=True)
# print(t)  # [9, 8, 7, 6, 5, 1, 2, 3, 4]