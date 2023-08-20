# Цикл for Часть 1.

# for i in "String text":
#     print(i)
# print("Программа работает дальше")


# m = "String text"
# for i in m:
#     if i == "t":
#         print("В строке есть буква t")
# else:
#     print("Цикл завершен")
#
# print("Программа работает дальше")

# m = "String text"
# count = 0
# for i in m:
#     if i == "t":
#         print("В строке есть буква t")
#         count += 1
# else:
#     print("Цикл завершен, букв t", count)
#
# print("Программа работает дальше")

# m = "String text"
# count = 0
# for i in m:
#     if i == "t":
#         print("В строке есть буква t")
#         count += 1
#     if i == "g":
#         break   # Оператор break прерывает цикл до срочно.
# else:
#     print("Цикл завершен, букв t", count)
#
# print("Программа работает дальше")


m = "String text"
count = 0
for i in m:
    if i == "t":
        continue   # Оператор continue прерывает итерацию, цикл продолжает работать дальше.
        print("В строке есть буква t")
        count += 1
    print(i)

else:
    print("Цикл завершен, букв t", count)

print("Программа работает дальше")
