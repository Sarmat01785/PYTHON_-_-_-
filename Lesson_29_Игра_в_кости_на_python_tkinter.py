# Игра в кости на python tkinter

import tkinter as tk
from random import randint

# Создаем окно и виджеты
window = tk.Tk()
window.title("Игра в кости")

label = tk.Label(window, text="Игра в кости", font=("Arial", 24))
label.pack(pady=10)

dice_label = tk.Label(window, text="Бросьте кости!", font=("Arial", 18))
dice_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 18))
result_label.pack(pady=10)

# Функция для броска костей
def roll_dice():
    # Генерируем случайные числа от 1 до 6
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)

    # Обновляем текст на метке с результатом
    result_label.config(text=f"Выпало {dice1} и {dice2}!")

# Создаем кнопку для броска костей
roll_button = tk.Button(window, text="Бросить кости", command=roll_dice)
roll_button.pack(pady=10)

# Запускаем главный цикл окна
window.mainloop()


# from tkinter import *
# import random
# import os

# def bros():
#     images = ["b.png", "b2.png", "b3.png", "b4.png", "b5.png", "b6.png"]
#     while True:
#         x = random.choice(images)
#         if os.path.exists(x):
#             return x

# def img(event):
#     global b_1, b_2
#     for i in range(18):
#         b_1 = PhotoImage(file=bros())
#         b_2 = PhotoImage(file=bros())
#         lab_1["image"] = b_1
#         lab_2["image"] = b_2
#         root.update()
#         root.after(120)  # 120 миллисекунд (0.12 секунды)

# root = Tk()
# root.geometry("400x200")
# root.title("Игра в кости. Сделай бросок!!!")
# root.resizable(height=False, width=False)
# root.iconphoto(True, PhotoImage(file="iconka.png"))
# font = PhotoImage(file="holst.png")
# Label(root, image=font).pack()
# lab_1 = Label(root)
# lab_1.place(relx=0.3, rely=0.5, anchor=CENTER)
# lab_2 = Label(root)
# lab_2.place(relx=0.7, rely=0.5, anchor=CENTER)
# root.bind("<1>", img)

# root.mainloop()
