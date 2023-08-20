# Цикл while
# x = 0
# while x < 5:
#     x +=1
#     print(x)

# x = 0
# while x < 5:
#     x += 1
# else:
#     print(x)


# Факториал числа.
# x = int(input("Введите число: "))
# count = 0
# y = 1
# while count < x:
#     count += 1
#     y *= count
# else:
#     print(y)

# while True:
#     x = int(input("Введите число: "))
#     count = 0
#     y = 1
#     while count < x:
#         count += 1
#         y *= count
#     else:
#         print(y)

# x = ""
# while len(x) < 5:
#     y = input("ввод данных: ")
#
#     x += y
# else:
#     print(x)

# x = ""
# while len(x) < 5:
#     y = input("ввод данных: ")
#     if y == "o":
#         continue
#
#     x += y
# else:
#     print(x)

x = ""
while len(x) < 5:
    y = input("ввод данных: ")
    if y == "o":
        continue
    if y == "l":
        break

    x += y
else:
    print(x)
print("Программа работает дальше ")

