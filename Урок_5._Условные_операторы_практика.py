# Условные операторы Практика. Примеры использования модулей.

import webbrowser
# Запрашиваем у пользователя ввод адреса сайта.
website = input("Введите адрес сайта: ")

# Проверяем, содержит ли введенный адрес префикс "https://".
if "https://" in website:
    # Если адрес уже содержит префикс "https://", открываем его в браузере.
    webbrowser.open(website)
    result = "Адрес содержит 'https://'."
elif "www." in website:
    # Если адрес содержит "www.", проверяем, начинается ли он с "www." и добавляем "https://", если это необходимо.
    website = f"https://{website}" if not website.startswith("https://") else website
    webbrowser.open(website)
    result = "Адрес содержит 'www.' и был дополнен до полной формы."
else:
    # Если адрес не содержит "https://" и не начинается с "www.", добавляем их.
    website = f"https://www.{website}"
    webbrowser.open(website)
    result = "Адрес не содержал 'https://', и был дополнен до полной формы."

print(result)

# Пример остановки программы на 5 секунд используя модуль time
# import time
# time.sleep(5)  # Останавливаем исполнение программы на 5 секунд.

# Пример открытия внешней программы используя модуль os
# import os
# program_path = "C:/Program Files/путь_к_программе.exe"  # Замените на реальный путь к программе
# os.startfile(program_path)  # Открывает программу
