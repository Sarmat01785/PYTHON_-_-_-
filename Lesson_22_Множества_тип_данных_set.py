# Пересечения множеств
z = {1, 2, 3, 4, 5}
x = {3, 4, 5, 6, 7}
t = z.intersection(x)  # Находим общие элементы между множествами z и x
print(t)  # Выводит {3, 4, 5}

# Разница множеств
e = z.difference(x)  # Находим элементы, присутствующие в z, но отсутствующие в x
e_1 = x.difference(z)  # Находим элементы, присутствующие в x, но отсутствующие в z
print(e)  # Выводит {1, 2}
print(e_1)  # Выводит {6, 7}

# Для автоматического создания файла, если он не существует, используйте режим "a+"
# Этот режим позволяет читать и писать в файл, создавая его, если он не найден
with open('text.txt', 'a+') as r:
    r.seek(0)  # Перемещаем курсор в начало файла перед чтением
    new = set(r.read().split())

with open('text2.txt', 'a+') as r:
    r.seek(0)  # Перемещаем курсор в начало файла перед чтением
    new.update(r.read().split())

print(new)  # Выводит объединенное множество слов из обоих файлов

# Находим пересечение слов из двух файлов
with open('text.txt', 'a+') as r:
    r.seek(0)
    r_1 = set(r.read().split())

with open('text2.txt', 'a+') as r:
    r.seek(0)
    r_2 = set(r.read().split())

new_intersect = r_1.intersection(r_2)
print(new_intersect)  # Выводит множество слов, общих для обоих файлов

# Находим слова, уникальные для первого файла (text.txt)
with open('text.txt', 'a+') as r:
    r.seek(0)
    r_1 = set(r.read().split())

with open('text2.txt', 'a+') as r:
    r.seek(0)
    r_2 = set(r.read().split())

unique_to_first_file = r_1.difference(r_2)
print(unique_to_first_file)  # Выводит множество слов, уникальных для первого файла

# Находим слова, уникальные для второго файла (text2.txt)
with open('text.txt', 'a+') as r:
    r.seek(0)
    r_1 = set(r.read().split())

with open('text2.txt', 'a+') as r:
    r.seek(0)
    r_2 = set(r.read().split())

unique_to_second_file = r_2.difference(r_1)
print(unique_to_second_file)  # Выводит множество слов, уникальных для второго файла
