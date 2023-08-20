# Списки, методы типа данных list

# n = list(range(10))
# m = []
# for i in n:
#     if i == 8:
#         continue
#     m.append(i)
# else:
#     print(m)


# x = [9, 8, 7, 6, 5]
# x.append(4)  # Добавляет элемент в список.
# x.insert(1, 7)  # Вставляет элемент по указанному индексу.
# print(x.count(7))  # Метод count показывает сколько элементов в списке (в данном случае сколько 7)
# x.sort()  # Сортирует список по возрастанию.
# x.reverse()  # Переворачивает в обратную сторону.
# y = x.pop(0)  # Удаляет элемент по индексу. Если в скобках не чего не указать, то будет удален последний элемент.
# x.remove(7)   # Удаляет указанный элемент. Только один раз.
# x.clear()     # Метод очищает список.
# x.extend(["a", "s"])  # Добавляет в конец списка значение из другого списка.
# h = x.copy()   # Копирует список.
# print(y)
# print(x)
# print(h)

# Составить новый список с четными числами, а в списки n оставить нечетные числа.
# n = list(range(1, 21))
# m = []
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)


# n = list(range(1, 21))
# b = n.copy()
# m = []
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
# print(b)


# n = list(range(1, 21))
# b = n[::]
# m = []
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
# print(b)

# n = list(range(1, 21))
# b = n[0::2]      # Срезы с шагом 2. В списки b получаются все нечетные числа.
# m = []
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
# print(b)


# n = list(range(1, 21))
# b = n[1::2]      # Срезы с шагом 2. В списки b получаются все четные числа.
# m = []
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
# print(b)


# n = list(range(1, 21))
# b = n[::5]      # Срезы
# m = []
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
# print(b)


n = list(range(1, 21))
b = n[5:]      # Срезы
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)
