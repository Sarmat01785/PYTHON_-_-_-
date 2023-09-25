# Функции, область видимости переменных

# x = 5
# count = 0
# while count < 3:
#     count +=1
# print(count)


# x = 5

# def name():
#     print(x)
# name()


# x = 5

# def name():
#     y = 10 # Переменная объявленная в функци существует только в функции
#     print(x)

# name()
# print(y) #   print(y)
#              # NameError: name 'y' is not defined  Возникает ошибка


# x = 5

# def name():
#     y = 10 # Переменая y существует только в локальной скрытой области функции
#     print(x) # 5
#     return y

# h = name()
# print(h) # 10
# # print(y) # NameError: name 'y' is not defined переменная y как была не доступеа так и есть
# # из глобальной области видимости переменная y недоступна


# x = 5

# def name():
#     x = 10
#     print(x) # 10
# name()
# print(x) # 5


# x = 5

# def name():
#     x += 10
#     print(x) # UnboundLocalError: local variable 'x' referenced before assignment возникает ошибка
# name()
# print(x)


# x = 5

# def name():
#     global x # Ключевым словом global мы даем команду что мы не создаем новую локальную переменную, а мыхотим внести изменения
#     # глобальную переменную x
#     x = 100
#     print(x) # 100
# name()
# print(x)  # 100


# x = 5

# def name():
#     global x
#     x = 100
#     print(x)  # 100
# name()
# print(x)  # 100

# def name_2():
#     print(x) # 100
# name_2()     # 100


# x = 5


# def name():
#     x = 100
#     return x


# h = name()


# def name_2():
#     print(h)


# name_2() # 100


# x = 5


# def name():
#     x = 100
#     return name_2(x)


# def name_2(par):
#     print(par)


# name() # 100


# Функция объявлена в функции
# x = 5  # глобальная область видемости


# def name():
#     x = 10  # локальная область видемости

#     def neme_2():
#         x = 100
#         print(x) # 100

#     neme_2()
#     print(x) # 10
# name()
# print(x) # 5


x = 5  # глобальная область видемости


def name():
    x = 10  # локальная область видемости

    def neme_2():
        nonlocal x
        x = 100
        print(x) # 100

    neme_2()
    print(x) # 100
name()
print(x) # 5