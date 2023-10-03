# Словари, тип данных dict()
# Часть 1. Варианты и методы

# d1={"a": 7}
# d2 = dict (a = 7)
# d1["b"] = 9
# d1["a"] = 8

# print(d1)  # {'a': 7, 'b': 9}
# print(d1['a']) # 8
# print(d1) # {'a': 7, 'b': 9}
# print(d2) # {'a': 7}
# print(d1) # {'a': 8, 'b': 9}


# d1={"a": 7}
# d2 = dict (a = 7)
# d1["b"] = 9
# del d1["a"]

# print(d1)  # {'b': 9}
# print(d2)  # {'a': 7}


# d1={"a": 7}
# d2 = dict (a = 7)

# print(d1)  # {'a': 7}
# print(d2)  # {'a': 7}


# d3 = dict.fromkeys([1, 2, 3, 4, 5]) # Метод fromkeys помогает нам создать словарь из ключей со значением по умолчанию
# print(d3) # {1: None, 2: None, 3: None, 4: None, 5: None} ключи 1,2,3,4,5 значение по умолчанию None


# d3 = dict.fromkeys([1, 2, 3, 4, 5], "value")
# print(d3) # {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value'}


# price = {'мясо': 3, 'хлеб': 1, 'картошка': 0.5, 'вода': 0.2}

# def buy():
#     pay = 0
#     while True:
#         enter = input('Что покупаем???\n')
#         if enter == 'end':
#             break
#         if enter in price:
#             pay += price[enter]
#         else:
#             print('Такого товара нет в списке!')
#     return pay

# print(buy())


# users = {
#     "Alex7": {"password": 9856214, "id": 1957},
#     "Jimmy99": {"password": 1236487, "id": 9654},
#     "Bob33": {"password": 9546752, "id": 6453},
# }

# print(users["Alex7"]["password"]) # 9856214


# d2 = dict([[1, 2], [3, 4], [5, 6]])
# print(d2)  # {1: 2, 3: 4, 5: 6}


# d1 = {"a": 7, "b": 9}
# d2 = dict([[1, 2], [3, 4], [5, 6]])
# d5 = d1.copy()  # Метод copy создает копию словаря
# print(d1.items()) # Возвращает список из картежей   dict_items([('a', 7), ('b', 9)])
# print(d1.keys())  # Взвращает ключи в словаре в виде списка  dict_keys(['a', 'b'])
# print(d1.values()) # Возвращает значения в словаре в виде списка  dict_values([7, 9])
# d1.update(d2)
# print(d1)  # {'a': 7, 'b': 9, 1: 2, 3: 4, 5: 6}


d1 = {"a": 7, "b": 9}
d2 = dict([[1, 2], [3, 4], [5, 6]])

if "c" in d1:
    d1["c"]

y = d1.get("c", "value")
print(y)  # value

t = d1.pop("a")
print(t, d1) # 7 {'b': 9}
