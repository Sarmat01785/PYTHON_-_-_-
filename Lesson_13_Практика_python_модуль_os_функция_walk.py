# Практика Python: использование модуля os и функции walk

import os
import time


# Функция для получения списка всех файлов в каталоге за последние 24 часа
def get_recent_files(directory, timeframe=86400):
    recent_files = []
    for address, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.abspath(os.path.join(address, file))
            # Проверяем, что файл был создан в течение последних 24 часов
            if time.time() - os.path.getctime(full_path) < timeframe:
                recent_files.append(full_path)
    return recent_files


# Замените "C:\Users\Сармат\Pictures" на путь к вашей целевой папке
files = get_recent_files(r"C:\Users\Сармат\Pictures")
print(files)


# Функция для получения списка файлов с определенным расширением
def get_files_with_extension(directory, extension):
    return [os.path.join(address, file)
            for address, dirs, files in os.walk(directory)
            for file in files if file.lower().endswith(f".{extension.lower()}")]


# Получаем список файлов JPG
jpg_files = get_files_with_extension(r"C:\Users\Сармат\Pictures", 'jpg')
print(jpg_files)
