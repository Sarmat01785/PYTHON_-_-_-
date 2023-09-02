#  Условные операторы Практика. Примеры использования модулей.

import os  # Импортируем модуль os для работы с операционной системой.

website = input("Введите адрес сайта: ")  # Запрашиваем у пользователя ввод адреса сайта.

if "https://" in website:  # Проверяем, содержит ли введенный адрес "https://". 
    os.system("start " + website)  # Запускаем веб-браузер с указанным адресом.
    print("if")  # Выводим сообщение "if".
elif "www." in website:  # Если адрес не содержит "https://" и содержит "www.".
    website = "https://" + website  # Добавляем префикс "https://" к адресу.
    os.system("start " + website)  # Запускаем веб-браузер с указанным адресом.
    print("elif")  # Выводим сообщение "elif".
else:  # Если адрес не содержит ни "https://" ни "www.".
    website = "https://www." + website  # Добавляем префиксы "https://" и "www." к адресу.
    os.system("start " + website)  # Запускаем веб-браузер с указанным адресом.
    print("else")  # Выводим сообщение "else".




# import webbrowser
# import time
# import os

# url = "https://www.youtube.com/"
# webbrowser.open(url)

# Останавливает исполнение программы на 5 секунд.
# time.sleep(5)

# Открывает программу с помощью функции startfile
# program_path = "C:/Program Files/путь_к_программе.exe"  # Замените на реальный путь к программе
# os.startfile(program_path)


