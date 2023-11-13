# Условные операторы if, elif, else
"""
Условные операторы if, elif и else позволяют вам выполнять различные действия в зависимости от условий. 
Они позволяют программе 
принимать решения на основе определенных критериев.
"""

# Оператор if позволяет выполнить блок кода, только если условие истинно.
# пример:
age = 18

if age >= 18:
    print("Вы совершеннолетний")


# Оператор elif позволяет добавить дополнительные условия для проверки,
# если предыдущие условия были ложными.
# пример:
age = 16

if age >= 18:
    print("Вы совершеннолетний")
elif age >= 13:
    print("Вы подросток")
else:
    print("Вы ребенок")


# Оператор else выполняется, если все предыдущие условия были ложными.
# пример:
age = 10

if age >= 18:
    print("Вы совершеннолетний")
else:
    print("Вы несовершеннолетний")



# if True:
#     print("if")
# elif True:
#     print("True")
# else:
#     print("else")

# if False:
#     print("if")
# elif True:
#     print("True")
# else:
#     print("else")

# if False:
#     print("if")
# elif False:
#     print("True")
# else:
#     print("else")


# x = 0
# if x == 0:
#     print("if")
# elif x > 0:
#     print("True")
# else:
#     print("else")


# x = 3
# if x == 0:
#     print("if")
# elif x > 0:
#     print("True")
# else:
#     print("else")

# x = -5
# if x == 0:
#     print("if")
# elif x > 0:
#     print("True")
# else:
#     print("else")

# x = 5
# if x == 0:
#     x += 1
# print(5 / x)


x = 0
if x == 0:
    x += 1
print(5 / x)
