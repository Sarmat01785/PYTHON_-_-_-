# Функции переменное количество аргументов, параметр *args

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


def exclusiv_item(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key == True:
        new_list.sort
        
            
        
    return new_list

z = [9, 8, 7]
x =[8, 8, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

t = exclusiv_item(z, x, c, key=True)
print(t)  # [9, 8, 7, 6, 5, 1, 2, 3, 4]