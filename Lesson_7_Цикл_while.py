# Цикл while
# Программа запрашивает ввод адреса сайта и открывает его в браузере.
# Чтобы завершить программу, пользователь должен ввести "Завершить".

import webbrowser

print("Введите 'Завершить' для выхода из программы.")
while True:
    website = input("Введите адрес сайта: ")
    if website.lower() == "завершить" or website == "":  # .lower() позволяет принимать "Завершить" в любом регистре
        break
    if "https://" not in website:
        if "www." not in website:
            website = f"https://www.{website}"  # Предполагаем, что адрес должен начинаться с https://www.
        else:
            website = f"https://{website}"  # Добавляем только префикс https://
    webbrowser.open_new(website)  # Открываем сайт в новом окне браузера
