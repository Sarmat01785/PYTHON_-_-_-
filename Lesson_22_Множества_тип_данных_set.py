# Множества, тип данных set()
# Множества, практическое применение

# t = {"a", "f", 1, 2, 3, 25, (2, 5)}  # Множества это не упорядочное количество элементов.

# print(t)  # {1, 2, 3, 'f', 25, (2, 5), 'a'}
# print(type(t))  # <class 'set'>

# y = set() # Множество


# t = {"a", "f", 1, 1 , 1, 1, 2, 3, 25, (2, 5)}  # Множества это не упорядочное количество элементов.

# print(t)  # {'a', 1, 2, 3, 'f', 25, (2, 5)}  Множество содержит только уникальные элементы, все повторяющиеся будут отсеиваться.
# print(type(t))  # <class 'set'> У множества отсудствует индексация, можно работать толко при помощи метадов.


# x = (1, 2, 3, 4, 5, 6, 7) # Кортеж
# y = [1, 2, 3, 4, 5, 6, 7] # Список
# u = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7} # Словарь
# h = {1, 2, 3, 4, 5, 6, 7} # Множества

# print(x.__sizeof__())  # 80
# print(y.__sizeof__())  # 104
# print(u.__sizeof__())  # 344
# print(h.__sizeof__())  # 456


# import time


# def f(*args):
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#         return list_new


# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))

# start = time.time()
# f(z, x, c)
# stop = time.time() - start
# print(stop)  # 0.38080739974975586

# start_2 = time.time()
# r = set(z)
# t = r.union(set(x), set(c))
# stop_2 = time.time() - start_2
# print(stop_2)  # 0.0010039806365966797


# z = {1, 2, 3, 4, 5}
# z.add(6) # Метод add добовление элемента во множества
# z.discard(6) # Метод discard позволяет удалить элемент множества
# # z.remove(6)  # Метод remove позволяет удалить элемент множества

# print(z) # {1, 2, 3, 4, 5, 6}


# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}

# y = z.union(x)  # Объединения множеств


# print(y)  # {1, 2, 3, 4, 5, 6, 7}


# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}

# z.update(x) # Объединения множеств


# print(z)  # {1, 2, 3, 4, 5, 6, 7}


# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}

# t = z.intersection(x)  # Пересечения множеств


# print(t)  # {3, 4, 5} общие элементы между множествами.


# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}


# e = z.difference(x)  # Разница множеств
# e_1 = x.difference(z)  # Разница множеств

# print(e)  # {1, 2} т.е. элементы 1 и 2 не встречаються во множестве x
# print(e_1)  # {6, 7} т.е. элементы 6 и 7 не встречаються во множестве z



# new = set()

# r = open('text.txt')
# new.update(set(r.read().split()))
# r.close()

# r = open('text2.txt')
# new.update(set(r.read().split()))
# r.close()

# print(new)




# r = open('text.txt')
# r_1 = (set(r.read().split()))
# r.close()

# r = open('text2.txt')
# r_2 = (set(r.read().split()))
# r.close()

# new = r_1.intersection(r_2)

# print(new)


# r = open('text.txt')
# r_1 = (set(r.read().split()))
# r.close()

# r = open('text2.txt')
# r_2 = (set(r.read().split()))
# r.close()

# new = r_1.difference(r_2)

# print(new)


r = open('text.txt')
r_1 = (set(r.read().split()))
r.close()

r = open('text2.txt')
r_2 = (set(r.read().split()))
r.close()

new = r_2.difference(r_1)

print(new)