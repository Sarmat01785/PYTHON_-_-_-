# Менеджер контекста with as
# Суть применения

# r = open('file.txt', 'a', encoding='utf-8')
# r.write('something' + '\n')
# r.write('что-то')
# r.close()

# print('Все норм')


# with open("file.txt", "a", encoding="utf-8") as r:
#     r.write("something" + "\n")

#     r.write("что-то")
# print("Все норм")


# r = open('file.txt', 'a', encoding='utf-8')
# try:
#     r.write('something' + '\n')
#     r.write('что-то')
# finally:
#     r.close()

# print('Все норм')


# Открываем файл "file.txt" в режиме добавления (append) и указываем кодировку utf-8.
# Используем оператор "with", чтобы автоматически закрыть файл после завершения операций.
with open("file.txt", "a", encoding="utf-8") as r:
    # Записываем строку "something" в файл и добавляем символ новой строки.
    r.write("something" + "\n")

    # Записываем строку "что-то" в файл.
    r.write("что-то")

# Выводим сообщение "Все норм" в консоль.
print("Все норм")
