# Тема урока: Функция `sample()` в Python

Функция `sample()` из модуля `random` используется для получения случайной выборки элементов из итерируемых объектов,
таких как списки, кортежи или строки. Она возвращает новый список, содержащий уникальные элементы исходной коллекции.

### Импорт модуля `random`

Для начала импортируем модуль `random`, чтобы иметь доступ к функции `sample()`.


```python
import random
```

### Пример 1: Получение одного случайного элемента из списка

Мы можем получить один случайный элемент из списка, передав второй аргумент функции `sample()` равным 1.


```python
# Пример 1: Получение одного случайного элемента из списка
my_list = [1, 2, 3, 4, 5]
random_element = random.sample(my_list, 1)
print(random_element)  # Выводит список с одним случайным элементом, например: [2]
```

    [4]
    

### Пример 2: Получение нескольких случайных элементов из списка

Чтобы получить несколько случайных элементов, мы просто изменяем второй аргумент функции `sample()`.


```python
# Пример 2: Получение нескольких случайных элементов из списка
random_elements = random.sample(my_list, 3)
print(random_elements)  # Выводит список из трех случайных элементов, например: [4, 1, 5]
# Обратите внимание, что количество элементов в результате соответствует второму аргументу функции sample().
```

    [1, 3, 2]
    

### Пример 3: Получение случайного символа из строки

Функцию `sample()` можно применять не только к спискам, но и к строкам.


```python
# Пример 3: Получение случайного символа из строки
my_string = "Hello, World!"
random_character = random.sample(my_string, 1)
print(random_character)  # Выводит список с одним случайным символом, например: ['e']
```

    ['d']
    

### Обработка ошибок

Если попытаться выбрать больше элементов, чем есть в исходной коллекции, будет возбуждено исключение `ValueError`.


```python
# Вызов sample() с количеством элементов, превышающим размер исходной коллекции, приведет к ValueError.
try:
    too_many_elements = random.sample(my_list, 10)
except ValueError as e:
    print("Ошибка:", e)  # Выведет сообщение об ошибке
```

    Ошибка: Sample larger than population or is negative
    

### Полезность функции `sample()`

Функция `sample()` полезна в ситуациях, где требуется случайная выборка без повторений, например:
- При разработке игр
- В статистических моделях
- Для случайного разбиения данных на подгруппы

Важно помнить, что элементы, возвращаемые функцией `sample()`, не повторяются, в отличие от функции `choice()`, которая может вернуть один и тот же элемент несколько раз при многократном вызове.
