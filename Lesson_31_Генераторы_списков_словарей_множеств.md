## Использование `Comprehensions` в Python для создания новых коллекций из существующих

Comprehension — это удобная и мощная техника в Python для создания новых списков, множеств или словарей на основе существующих последовательностей или итерируемых объектов. Рассмотрим несколько примеров использования comprehension для различных типов коллекций.

### Генерация списка

Исходный список чисел:


```python
numbers = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5, -2]
```

Создание нового списка, где каждое чётное число умножается на 2:


```python
even_numbers_doubled = [x * 2 for x in numbers if x % 2 == 0]
print(even_numbers_doubled)  # Выведет: [16, 8, 12, 4, -4]
```

    [16, 8, 12, 4, -4]
    

То же самое, но только с положительными числами:


```python
positive_even_numbers_doubled = [x * 2 for x in numbers if x % 2 == 0 and x > 0]
print(positive_even_numbers_doubled)  # Выведет: [16, 8, 12, 4]
```

    [16, 8, 12, 4]
    

### Генерация множества

Рассмотрим генерацию множества уникальных квадратов положительных чисел из списка:


```python
unique_squares = {x**2 for x in numbers if x > 0}
print(unique_squares)  # Выведет: {64, 49, 36, 25, 16, 9, 4, 1}
```

    {64, 1, 36, 4, 9, 16, 81, 49, 25}
    

### Генерация словаря

Исходный словарь с ценами:


```python
prices = {'мясо': 200, 'хлеб': 100, 'картофель': 50, 'вода': 20}
```

Обновление цен с 15% скидкой, используя словарный `comprehension`:


```python
discounted_prices = {item: round(price * 0.85, 2) for item, price in prices.items()}
print(discounted_prices)  # Выведет: {'мясо': 170.0, 'хлеб': 85.0, 'картофель': 42.5, 'вода': 17.0}
```

    {'мясо': 170.0, 'хлеб': 85.0, 'картофель': 42.5, 'вода': 17.0}
    

### Использование `os.walk()` для поиска файлов

Поиск всех файлов в корневой директории "C:\":


```python
import os

root_dir = "C:\\"
all_files = [os.path.join(root, name) for root, dirs, files in os.walk(root_dir) for name in files]
print(f"Найдено файлов: {len(all_files)}")
```

    Найдено файлов: 908148
    

Поиск всех файлов с расширением .txt в корневой директории "C:\":


```python
txt_files = [os.path.join(root, name) for root, dirs, files in os.walk(root_dir) for name in files if
             name.endswith('.txt')]
print(f"Найдено .txt файлов: {len(txt_files)}")
```

    Найдено .txt файлов: 6211
    

### Заключение

`Comprehension` — это очень полезный инструмент в Python, позволяющий создавать новые коллекции на основе существующих данных. Он значительно упрощает код и делает его более читабельным.
