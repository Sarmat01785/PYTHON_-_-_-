# Использование comprehensions в Python для создания новых коллекций из существующих

# Исходный список чисел
h = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5, -2]

# Создание нового списка, где каждое четное число умножено на 2
even_numbers_doubled = [x * 2 for x in h if x % 2 == 0]
print(even_numbers_doubled)  # Выведет: [16, 8, 12, 4, -4]

# То же самое, но только с положительными числами
positive_even_numbers_doubled = [x * 2 for x in h if x % 2 == 0 and x > 0]
print(positive_even_numbers_doubled)  # Выведет: [16, 8, 12, 4]

# Использование os.walk() для поиска всех файлов в корневой директории "C:\"

import os

all_files = [os.path.join(root, name) for root, dirs, files in os.walk("C:\\") for name in files]
print(f"Найдено файлов: {len(all_files)}")

# Поиск всех файлов с расширением '.txt' в корневой директории "C:\"
txt_files = [os.path.join(root, name) for root, dirs, files in os.walk("C:\\") for name in files if
             name.endswith('.txt')]
print(f"Найдено .txt файлов: {len(txt_files)}")

# Исходный словарь с ценами
price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

# Обновление цен с 15% скидкой, используя словарное включение
new_price = {item: round(value * 0.85, 2) for item, value in price.items()}
print(new_price)  # Выведет: {'meat': 1.7, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}
