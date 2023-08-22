# Функции def, параметры и аргументы

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


def count_list(parametr,parametr2 = False, count = 0):
    
    if parametr2 == True:
        typ = type(parametr[0])
        for i in parametr:
            count += 1
        return count, typ
    else:
        
        for i in parametr:
            count += 1
        return count
j = [9, 8, 7, 6]
print(count_list(j, True, -1))  # Можно изменить все три параметра в функции, передав все три аргумента.

