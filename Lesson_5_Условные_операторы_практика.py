# Условные операторы Практика. Примеры использования модулей.

import webbrowser
from urllib.parse import urljoin

# Запрашиваем у пользователя ввод адреса сайта.
website = input("Введите адрес сайта: ")

# Проверяем, содержит ли введенный адрес "https://".
if "https://" in website:
    # Запускаем веб-браузер с указанным адресом.
    webbrowser.open(website)
    result = "Адрес содержит 'https://'."
elif "www." in website:
    # Если адрес не содержит "https://" и содержит "www.", добавляем префикс "https://".
    website = urljoin("https://", website)
    webbrowser.open(website)
    result = "Адрес содержит 'www.' и был дополнен до полной формы."
else:
    # Если адрес не содержит ни "https://" ни "www.", добавляем префиксы "https://" и "www.".
    website = urljoin("https://www.", website)
    webbrowser.open(website)
    result = "Адрес не содержал ни 'https://', ни 'www.' и был дополнен до полной формы."

print(result)

# Пример остановки программы на 5 секунд используя модуль time
# import time
# time.sleep(5)  # Останавливаем исполнение программы на 5 секунд.

# Пример открытия внешней программы используя модуль os
# import os
# program_path = "C:/Program Files/путь_к_программе.exe"  # Замените на реальный путь к программе
# os.startfile(program_path)  # Открывает программу
