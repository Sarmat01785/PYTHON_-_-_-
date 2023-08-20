# Практика python, модуль os, функция walk - (позволяет сгенерировать пути ко
# всем файлам на компьютере.)


# import os
#
# for i in os.walk(r"C:\Users\Сармат\Documents\Обучение"):
#     print(i)
#     break


# import os
#
# for i in os.walk(r"C:\Users\Сармат\Documents\Обучение"):
#     print(i)

# import os
#
# list = []
# for address, dirs, files in os.walk(r"C:\Users\Сармат\Pictures"):
#     list.append(address)
# print(list)


# import os
#
# list = []
# for address, dirs, files in os.walk(r"C:\Users\Сармат\Pictures"):
#     for file in files:
#         list.append(os.path.join(address, file))
# print(list)


# import os
#
# list = []
# for address, dirs, files in os.walk(r"C:\Users\Сармат\Pictures"):
#     for file in files:
#         full = os.path.join(address, file)
#         if "jpg" in full:
#             list.append(full)
# print(list)


import os
import time

list = []
for address, dirs, files in os.walk(r"C:\Users\Сармат\Pictures"):
    for file in files:
        full = os.path.join(address, file)
        if time.time() - os.path.getctime(full) < 86400:
            list.append(full)
print(list)
