import webbrowser

print("Введите 'Завершить' для выхода из программы.")
while True:
    website = input("Введите адрес сайта: ").strip()  # Удаляем лишние пробелы
    if website.lower() == "завершить" or website == "":
        print("Программа завершена.")
        break
    if not website.startswith(("http://", "https://")):
        # Добавляем префикс https:// для корректности URL
        website = f"https://{website}"
    webbrowser.open(website)  # Открываем сайт в новой вкладке браузера