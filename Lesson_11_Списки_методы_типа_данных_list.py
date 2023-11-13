# Списки, методы типа данных list

'''
Списки - это один из самых основных типов данных в Python. Они позволяют хранить набор элементов 
в упорядоченной последовательности.

Чтобы создать список в Python, вы можете перечислить элементы в квадратных скобках, разделяя их запятыми. 
'''
# Например:
numbers = [1, 2, 3, 4, 5]

# Также можно создать пустой список и добавить элементы позже:
fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")
'''
Одним из основных методов списка является append(), который позволяет добавить элемент в конец списка.
'''


'''
Также существует ряд других полезных методов, которые можно использовать с типом данных list:

- len(): возвращает количество элементов в списке.
- index(): возвращает индекс первого вхождения указанного элемента.
- count(): возвращает количество вхождений указанного элемента.
- sort(): сортирует список по возрастанию.
- reverse(): меняет порядок элементов списка на обратный.
- remove(): удаляет первое вхождение указанного элемента.
'''

# Вот примеры, демонстрирующие использование этих методов:
numbers = [5, 2, 8, 1, 3]
print(len(numbers))  # Выводит: 5

fruits = ["apple", "banana", "orange", "apple"]
print(fruits.index("orange"))  # Выводит: 2

print(fruits.count("apple"))  # Выводит: 2

numbers.sort()
print(numbers)  # Выводит: [1, 2, 3, 5, 8]

fruits.reverse()
print(fruits)  # Выводит: ["apple", "orange", "banana", "apple"]

fruits.remove("banana")
print(fruits)  # Выводит: ["apple", "orange", "apple"]




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
