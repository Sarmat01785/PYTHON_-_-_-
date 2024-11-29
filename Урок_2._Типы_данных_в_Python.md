### Типы данных в Python
- Python поддерживает различные типы данных, позволяющие хранить и обрабатывать разнообразные значения:

### Числовые типы данных


```python
x = 5  # Целое число (int)
y = -10  # Целое число (int)
PI = 3.14  # Вещественное число (float)
temperature = 25.5  # Вещественное число (float)
complex_number = 1 + 1j  # Комплексное число (complex)
```


```python
print(x)
print(type(x))
```

    5
    <class 'int'>
    


```python
print(y)
print(type(y))
```

    -10
    <class 'int'>
    


```python
print(PI)
print(type(PI))
```

    3.14
    <class 'float'>
    


```python
print(temperature)
print(type(temperature))
```

    25.5
    <class 'float'>
    


```python
print(complex_number)
print(type(complex_number))
```

    (1+1j)
    <class 'complex'>
    

### Строковый тип данных


```python
message = "Привет, мир!"  # Строка (str)
name = 'Alice'  # Строка (str)
```


```python
print(message)
print(type(message))
```

    Привет, мир!
    <class 'str'>
    


```python
print(name)
print(type(name))
```

    Alice
    <class 'str'>
    

### Коллекции


```python
numbers = [1, 2, 3, 4, 5]  # Список (list)
fruits = ['яблоко', 'банан', 'апельсин']  # Список (list)
coordinates = (10, 20)  # Кортеж (tuple)
person = ('John', 25, 'Москва')  # Кортеж (tuple)
student = {'имя': 'Alice', 'возраст': 20, 'курс': 'Python'}  # Словарь (dict)
country = {'название': 'Россия', 'столица': 'Москва', 'население': 12000000}  # Словарь (dict)
set_1 = {1, 2, 3, 4}  # Множество (set)
set_2 = {'яблоко', 'банан', 'апельсин'}  # Множество (set)
```


```python
print(numbers)
print(type(numbers))
```

    [1, 2, 3, 4, 5]
    <class 'list'>
    


```python
print(fruits)
print(type(fruits))
```

    ['яблоко', 'банан', 'апельсин']
    <class 'list'>
    


```python
print(coordinates)
print(type(coordinates))
```

    (10, 20)
    <class 'tuple'>
    


```python
print(person)
print(type(person))
```

    ('John', 25, 'Москва')
    <class 'tuple'>
    


```python
print(student)
print(type(student))
```

    {'имя': 'Alice', 'возраст': 20, 'курс': 'Python'}
    <class 'dict'>
    


```python
print(country)
print(type(country))
```

    {'название': 'Россия', 'столица': 'Москва', 'население': 12000000}
    <class 'dict'>
    


```python
print(set_1)
print(type(set_1))
```

    {1, 2, 3, 4}
    <class 'set'>
    


```python
print(set_2)
print(type(set_2))
```

    {'банан', 'яблоко', 'апельсин'}
    <class 'set'>
    

### Отсутствие данных и логические значения


```python
a = None  # NoneType: отсутствие значения
is_active = True  # Булево значение (bool)
is_closed = False  # Булево значение (bool)
```


```python
print(a)
print(type(a))
```

    None
    <class 'NoneType'>
    


```python
print(is_active)
print(type(is_active))
```

    True
    <class 'bool'>
    


```python
print(is_closed)
print(type(is_closed))
```

    False
    <class 'bool'>
    

### Ввод данных с клавиатуры и преобразование типов


```python
x = input("Ввод: ")  # Все введенные данные будут строкой (str)
r = int(x) + 5  # Преобразование строки в целое число (int) перед сложением
print(r)
```

    Ввод: 6
    11
    

### Ввод данных с плавающей точкой и их обработка


```python
x1 = float(input("Введите число: "))  # Преобразование введенной строки в число с плавающей точкой (float)
y1 = float(input("Введите число: "))
r = x1 + y1
print("Результат: " + str(r))  # Объединение строки с числом, преобразованное в строку
```

    Введите число: 1.5
    Введите число: 1.1
    Результат: 2.6
    
