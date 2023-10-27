# Обработка исключений, try, except
# try: except: finally

# while True:
#     try:
#         enter = float(input('Введите число: '))
#         break
#     except ValueError:
#         print('Вы ввели не число!!!')

# print('Все нормально')


# while True:
#     try:
#         enter = float(input('Введите число: '))
#         print(100/enter)
#         break
#     except ValueError:
#         print('Вы ввели не число!!!')
#     except ZeroDivisionError:
#         print('Делить на ноль нельзя!!!')

# print('Все нормально')


# while True:
#     try:
#         enter = float(input("Введите число: "))
#         print(100 / enter)

#     except ValueError:
#         print("Вы ввели не число!!!")
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!!!")
#     else:
#         print("Пользователь молодец, с первого раза!!!")
#     finally:
#         print('Вывод финали')

# print("Все нормально")


# while True:
#     try:
#         enter = float(input("Введите число: "))
#         print(100 / enter)

#     except ValueError:
#         print("Вы ввели не число!!!")

#     else:
#         print("Пользователь молодец, с первого раза!!!")
#     finally:
#         print("Вывод финали")

# print("Все нормально")


# import sys

# url_list = ['text.txt, text2.txt, text25.txt, text3.txt, ']

# list_defect = []
# list_info = []

# for url in url_list:
#     r = open(url)
#     print(r.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt, text2.txt, text25.txt, text3.txt, '


# import sys

# url_list = ["text.txt, text2.txt, text25.txt, text3.txt, "]

# list_defect = []
# list_info = []

# for url in url_list:
#     try:
#         r = open(url)
#         list_info.append(r.read())
#         print('Здесь')
#     except Exception:
#         list_defect.append(url)
#         print('тут')
#         continue


# import sys

# url_list = ["text.txt, text2.txt, text25.txt, text3.txt, "]

# list_defect = []
# list_info = []

# for url in url_list:
#     try:
#         r = open(url)
#         list_info.append(r.read())
#         print('Здесь')
#     except Exception:
#         list_defect.append(url)
#         print('тут')
#         sys.exit()
#         continue


import sys

url_list = ["text.txt, text2.txt, text25.txt, text3.txt, "]

list_defect = []
list_info = []

try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print("Здесь")
        except Exception:
            list_defect.append(url)
            print("тут")
            sys.exit()
        continue
finally:
    r = open("save.txt", "a")
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print("я все записал не смотря ни на что!!!")
    
    
    
    import sys  # Импорт модуля sys

url_list = ["text.txt, text2.txt, text25.txt, text3.txt, "]  # Создание списка url

list_defect = []  # Создание пустого списка для дефектных url
list_info = []  # Создание пустого списка для информации

try:  # Блок try
    for url in url_list:  # Цикл for для каждого url из списка url_list
        try:  # Вложенный блок try
            r = open(url)  # Открытие файла с url
            list_info.append(r.read())  # Добавление прочитанного содержимого файла в список list_info
            print("Здесь")  # Вывод строки "Здесь"
        except Exception:  # Блок except для перехвата исключений
            list_defect.append(url)  # Добавление дефектного url в список list_defect
            print("тут")  # Вывод строки "тут"
            sys.exit()  # Выход из программы
        continue  # Продолжение цикла
finally:  # Блок finally
    r = open("save.txt", "a")  # Открытие файла "save.txt" в режиме добавления
    for i in list_info:  # Цикл for для каждого элемента i в списке list_info
        r.write(i)  # Запись элемента i в файл
    r.write(str(list_defect))  # Запись списка list_defect в файл в виде строки
    r.close()  # Закрытие файла
    print("я все записал не смотря ни на что!!!")  # Вывод строки "я все записал не смотря ни на что!!!"
    
    
    '''
    Данный код осуществляет обработку списка URL-адресов для открытия файлов и записи их содержимого в файл "save.txt". 

1. Сначала импортируется модуль sys, который предоставляет функциональность для работы с системными параметрами и функциями.
2. Создаются переменные url_list, list_defect и list_info. url_list представляет собой список URL-адресов, 
list_defect - список дефектных URL-адресов, а list_info - список для хранения информации из файлов.
3. В блоке try осуществляется итерация по каждому URL-адресу из списка url_list.
4. Во вложенном блоке try происходит открытие файла с использованием указанного URL-адреса.
5. Если открытие файла происходит успешно, его содержимое считывается и добавляется в список list_info. 
Здесь также выводится строка "Здесь".
6. Если возникает исключение при открытии файла (например, файл не существует), URL-адрес добавляется в список list_defect, 
выводится строка "тут", и происходит выход из программы с помощью sys.exit().
7. Цикл продолжается, и происходит обработка следующего URL-адреса.
8. В блоке finally открывается файл "save.txt" в режиме добавления.
9. Цикл for проходит по каждому элементу list_info и записывает его содержимое в файл.
10. Затем список list_defect преобразуется в строку с помощью функции str() и записывается в файл.
11. Файл закрывается, и выводится строка "я все записал не смотря ни на что!!!".

Таким образом, данный код обрабатывает список URL-адресов, открывает соответствующие файлы, 
считывает их содержимое и записывает в файл "save.txt". В случае ошибки при открытии файла, программа прекращает выполнение.
    '''
