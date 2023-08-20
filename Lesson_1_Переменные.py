print("Lets,go!")

# переменные.
number = 4
number2 = 5
result = number + number2
print(result)

# Несколько переменных могут ссылаться на один и тот же объект в памяти.
num1 = num2 = 5
print(num1, num2)

# Множественное присвоение.
num_1, num_2 = 5, 7
print(num_1, num_2)

# Обмен данных между переменными.
swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1
print(swap1, swap2)

swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1 + swap2  # Так же можно делать математические операции.
print(swap1, swap2)

swap2 -= number  # swap2 = swap2 - number
print(swap2)

# Распаковка списка по переменно.
z, x, c = [1, 2, 3]
print(z)
print(x)
print(c)
print(z, x, c)

z, x, *c = [1, 2, 3, 4, 5]
print(z)
print(x)
print(c)
print(z, x, c)

z, *x, c = [1, 2, 3, 4, 5]
print(z)
print(x)
print(c)
print(z, x, c)

*z, x, c = [1, 2, 3, 4, 5]  # * - arg
print(z)
print(x)
print(c)
print(z, x, c)
