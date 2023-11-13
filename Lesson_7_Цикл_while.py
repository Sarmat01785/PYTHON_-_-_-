# Цикл while
# после каждого ввода сайта, программа будет запрашивать ввод сайта.

import os

while True:
    website = input("Введите адрес сайта\n ")
    if website == "Завершить":
        break
    if "https://" in website:
        os.system("start " + website)
        print("if")
    elif "www." in website:
        website = "https://" + website
        os.system("start " + website)
        print("elif")
    else:
        website = "https://www." + website
        os.system("start " + website)
        print("else")

