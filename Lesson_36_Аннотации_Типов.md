### Аннотации типов в `Python`

Аннотации типов позволяют указывать типы данных для переменных, параметров функций и возвращаемых значений. Это помогает повысить читаемость кода и облегчает его статический анализ инструментами вроде `mypy`.

#### Простая функция с аннотациями типов

Пример функции, которая принимает два целых числа и возвращает их сумму:


```python
def add_numbers(a: int, b: int) -> int:
    """Возвращает сумму двух целых чисел."""
    return a + b
```

Примечание:  
- a: int и b: int указывают, что параметры должны быть целыми числами.
- -> int обозначает, что функция возвращает целое число.

#### Работа со списками

Функция, принимающая список целых чисел и возвращающая их сумму:


```python
# Импортируем необходимые модули
from typing import List, Optional, Dict
```


```python
def sum_numbers(numbers: List[int]) -> int:
    """Суммирует все элементы списка чисел."""
    return sum(numbers)
```

Примечание:  
- List[int] означает, что аргумент numbers должен быть списком, содержащим целые числа.

#### Необязательные параметры

Функция, которая приветствует пользователя, но имя может быть опциональным:


```python
def greet(name: Optional[str] = None) -> str:
    """Приветствие пользователя. Если имя не передано, выводит стандартное сообщение."""
    if name is not None:
        return f"Hello, {name}"
    else:
        return "Hello, World!"
```

Примечание:  
- Optional[str] позволяет параметру name принимать значение типа str или None.

#### Работа со словарями

Функция, обрабатывающая данные из словаря, где ключи – целые числа, а значения – строки:


```python
def process_data(data: Dict[int, str]) -> None:
    """Обрабатывает данные из словаря и выводит пары ключ-значение."""
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")
```

Примечание:  
- Dict[int, str] указывает, что data должно быть словарем, где ключи – целые числа, а значения – строки.
- -> None показывает, что функция ничего не возвращает.

#### Примеры вызова функций


```python
# Вызываем функцию сложения
result = add_numbers(10, 20)
print(result)  # Выводит: 30

# Суммируем элементы списка
total = sum_numbers([1, 2, 3, 4, 5])
print(total)  # Выводит: 15

# Приветствуем пользователя
greeting = greet("John")
print(greeting)  # Выводит: Hello, John

# Обработка словаря
process_data({1: "один", 2: "два"})
# Выводит:
# Key: 1, Value: один
# Key: 2, Value: два
```

    30
    15
    Hello, John
    Key: 1, Value: один
    Key: 2, Value: два
    

#### Важный момент

Аннотации типов не проверяются во время выполнения программы. Их цель – помощь разработчикам и инструментам статического анализа при написании и проверке кода.
