# Чтение и запись файлов
# Чтение, запись, кодировка файлов


# 'r' открыть для чтения (по умолчанию)
# "t"открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи, содержимое файла удаляется, если файла нет, создается новый
# 'а' открыть для дозаписи в конец файла, если файла нет, создается новый
# "b" открыть в бинарном режиме
# "+" открыть для чтения и записи 'r+', "w+', "a+"


# Открываем файл для записи с указанием кодировки UTF-8
with open("text.txt", "w", encoding="utf-8") as file:
    file.write("Строка текста")

# Открываем файл для чтения с указанием кодировки UTF-8
with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Выводим содержимое файла
print(content)


# # Открываем файл для чтения с указанием кодировки UTF-8
# with open("text.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# # Выводим содержимое файла
# print(content)


# import os
# list_paths = []

# for adress, papka, file in os.walk('C:\\'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_paths.append(full_path)

# with open("text.txt", "w", encoding="utf-8") as file:
#     for x in list_paths:
#         file.write(x + "\n")
# file.close()


# import os  # Импортируем модуль os для работы с операционной системой

# list_paths = []  # Создаем пустой список для хранения путей к файлам

# # Проходимся по дереву директорий, начиная с 'C:\\'
# # Итерируемся по директориям, поддиректориям и файлам
# for адрес, папка, файлы in os.walk('C:\\'):
#     for i in файлы:
#         полный_путь = os.path.join(адрес, i)  # Генерируем полный путь к файлу
#         list_paths.append(полный_путь)  # Добавляем полный путь к файлу в список

# # Открываем файл "text.txt" в режиме записи с кодировкой UTF-8
# # Используем менеджер контекста для автоматической обработки операций с файлом
# with open("text.txt", "w", encoding="utf-8") as file:
#     for x in list_paths:  # Итерируемся по списку путей к файлам
#         file.write(x + "\n")  # Записываем каждый путь к файлу в файл, добавляя символ новой строки


# r = open("text.txt", encoding="utf-8")
# for i in r:
#     if "read.py" in i:
#         print(i)
# r.close()


# r = open("PuntoSwitcherSetup.exe", "rb")
# y = open("Копия PuntoSwitcherSetup.exe", "wb")

# while True:
#     var = r.read(1048576)
#     print(len(var))
#     if len(var) == 17:
#         break
#     y.write(var)

# print("Контроль")

# r.close()
# y.close()
