# Обработка исключений, try, except, finally

## Создание строки


```python
# Создаем строку
text = "Привет, мир!"
print(type(text))  # Выводим <class 'str'>, подтверждая, что переменная text является строкой
```

    <class 'str'>
    

## Доступ к символам строки


```python
# Доступ к первому и последнему символу строки
first_char = text[0]
last_char = text[-1]
print(f"Первый символ: '{first_char}', последний символ: '{last_char}'")
```

    Первый символ: 'П', последний символ: '!'
    

## Срезы строк


```python
# Срезаем часть строки
slice_1_to_5 = text[1:5]
slice_from_start_to_7 = text[:7]
slice_from_8_to_end = text[7:]

print(f"Срез с 2-го по 5-й символы: '{slice_1_to_5}'")
print(f"Срез с начала до 7-го символа: '{slice_from_start_to_7}'")
print(f"Срез с 8-го символа до конца: '{slice_from_8_to_end}'")
```

    Срез с 2-го по 5-й символы: 'риве'
    Срез с начала до 7-го символа: 'Привет,'
    Срез с 8-го символа до конца: ' мир!'
    

## Длина строки


```python
# Определяем длину строки
length_of_text = len(text)
print(f"Длина строки: {length_of_text}")
```

    Длина строки: 12
    

## Методы строк


```python
# Преобразуем строку в верхний и нижний регистр
uppercased_text = text.upper()
lowercased_text = text.lower()

# Заменяем подстроку в строке
replaced_text = text.replace("мир", "Вселенная")

print(f"Верхний регистр: '{uppercased_text}'")
print(f"Нижний регистр: '{lowercased_text}'")
print(f"Замена подстроки: '{replaced_text}'")
```

    Верхний регистр: 'ПРИВЕТ, МИР!'
    Нижний регистр: 'привет, мир!'
    Замена подстроки: 'Привет, Вселенная!'
    

## Пример использования конструкций try, except и finally


```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Ошибка: деление на ноль")  # Обработка исключения деления на ноль
finally:
    print("Конец программы")  # Блок finally выполнится в любом случае
```

    Ошибка: деление на ноль
    Конец программы
    

## Обработка исключений при вводе данных от пользователя


```python
while True:
    try:
        enter = float(input('Введите число: '))
        print(100 / enter)
        break
    except ValueError:
        print('Вы ввели не число! Попробуйте снова.')  # Обработка исключения неверного ввода
    except ZeroDivisionError:
        print('Делить на ноль нельзя! Попробуйте снова.')  # Обработка попытки деления на ноль
    finally:
        print('Попытка ввода завершена.')  # Информирование о завершении попытки
```

    Введите число:  s
    

    Вы ввели не число! Попробуйте снова.
    Попытка ввода завершена.
    

    Введите число:  1
    

    100.0
    Попытка ввода завершена.
    

## Пример использования блока else


```python
try:
    enter = float(input("Введите число: "))
    result = 100 / enter
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print(f"Результат деления: {result}")  # Выводится, если исключений не возникло
finally:
    print('Вывод финали')  # Выполняется в любом случае, независимо от наличия исключений
```

    Введите число:  15
    

    Результат деления: 6.666666666666667
    Вывод финали
    

## Обработка исключений при работе с файлами


```python
url_list = ["text.txt", "text2.txt", "text25.txt", "text3.txt"]
list_defect = []
list_info = []

for url in url_list:
    try:
        with open(url) as f:
            content = f.read()
            list_info.append(content)
    except FileNotFoundError:
        print(f"Файл {url} не найден.")
        list_defect.append(url)

print(f"Содержимое прочитанных файлов: {list_info}")
print(f"Список ненайденных файлов: {list_defect}")
```

    Файл text25.txt не найден.
    Файл text3.txt не найден.
    Содержимое прочитанных файлов: ['', '']
    Список ненайденных файлов: ['text25.txt', 'text3.txt']
    
