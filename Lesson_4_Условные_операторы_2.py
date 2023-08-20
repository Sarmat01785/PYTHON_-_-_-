# Условные операторы if, elif, else часть 2
# x = 0
# if x == 0:
#     x = 1
#     print("x был равен нулю")
# elif x == int or x == float:
#     print("x допустимое значение")
# else:
#     print("В x не допустимый тип данных")
#     x = 1
# print(100 / x)

# x = 5
# if x == 0:
#     x = 1
#     print("x был равен нулю")
# elif x == int or x == float:
#     print("x допустимое значение")
# else:
#     print("В x не допустимый тип данных")
#     x = 1
# print(100 / x)

x = [1, 2]
if x == 0:  # if not x = 0:   Оператор not меняет булевое значение на противоположенное.
    x = 1
    print("x был равен нулю")
elif x == int or x == float:    # Так же есть оператор and.
    print("x допустимое значение")
else:
    print("В x не допустимый тип данных")
    x = 1
print(100 / x)
