## Использование модуля pathlib для работы с файлами

Модуль `pathlib` представляет файловую систему в виде объектов, что упрощает процесс обработки путей и файлов. В этом примере мы используем `Path` из `pathlib` для поиска недавно измененных файлов и файлов с определенным расширением.


```python
from pathlib import Path
import time

# Функция для получения списка всех файлов, которые были изменены в последние `timeframe` секунд
def get_recent_files(directory, timeframe=86400):
    recent_files = []
    # Используем метод glob для поиска всех файлов в директории
    for path in Path(directory).rglob('*'):
        # Проверяем время создания файла
        if time.time() - path.stat().st_ctime < timeframe:
            recent_files.append(str(path))
    return recent_files

# Функция для получения списка всех файлов с определенным расширением
def get_files_with_extension(directory, extension):
    # Формируем шаблон поиска и возвращаем список файлов
    return [str(file) for file in Path(directory).rglob(f'*.{extension}')]

# Замените на путь к вашей целевой папке
target_directory = r"C:\Users\Сармат\Pictures"

# Получение и вывод списка недавних файлов
recent_files = get_recent_files(target_directory)
print("Недавние файлы:", recent_files)

# Получение и вывод списка файлов с расширением JPG
jpg_files = get_files_with_extension(target_directory, 'jpg')
print("Файлы JPG:", jpg_files)
```

## Заключение

Использование `pathlib` облегчает манипуляцию файлами и директориями. Методы `rglob` и `stat` позволяют нам фильтровать файлы по времени изменения и расширению, что делает `pathlib` полезным инструментом для работы со многими файлами.
