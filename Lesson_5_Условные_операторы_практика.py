# Условные операторы Практика. Примеры использования модулей.

import webbrowser  # Импортируем модуль webbrowser для работы с веб-браузерами.

# Запрашиваем у пользователя ввод адреса сайта.
website = input("Введите адрес сайта: ")

# Проверяем, содержит ли введенный адрес "https://".
if "https://" in website:
    # Запускаем веб-браузер с указанным адресом.
    webbrowser.open(website)
    print("Адрес содержит 'https://'.")
elif "www." in website:
    # Если адрес не содержит "https://" и содержит "www.", добавляем префикс "https://".
    website = f"https://{website}"
    webbrowser.open(website)
    print("Адрес содержит 'www.' и был дополнен до полной формы.")
else:
    # Если адрес не содержит ни "https://" ни "www.", добавляем префиксы "https://" и "www.".
    website = f"https://www.{website}"
    webbrowser.open(website)
    print("Адрес не содержал ни 'https://', ни 'www.' и был дополнен до полной формы.")

# Пример остановки программы на 5 секунд используя модуль time
# import time
# time.sleep(5)  # Останавливаем исполнение программы на 5 секунд.

# Пример открытия внешней программы используя модуль os
# import os
# program_path = "C:/Program Files/путь_к_программе.exe"  # Замените на реальный путь к программе
# os.startfile(program_path)  # Открывает программу
