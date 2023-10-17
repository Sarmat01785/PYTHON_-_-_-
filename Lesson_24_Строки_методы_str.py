# Строки, методы str

# s = 'stroka texta'
# print(s[0:5]) # strok
# print(s[5])   # a

# s = 'stroka texta'
# print('str' in s) # True
# print('sto' in s) # False


# s = 'stroka texta'

# print(s.upper())  # STROKA TEXTA метод upper позволяет перевести все буквы в верхний регистор


# s = 'STroka texta'

# print(s.upper()) # STROKA TEXTA
# print(s.lower()) # stroka texta


# s = "sTroka texta"
# print(s.capitalize())  # Stroka texta метод capitalize переводит первую букву строки в верхний регистор
# print(s)  # sTroka texta


# s = "sTroka texta"

# s_1 = s.upper()   # Все в верхний регистр
# print(s_1)        # STROKA TEXTA
# s_2 = s.lower()   # Все в нижний регистр
# print(s_2)        # stroka texta
# s_3 = s.capitalize()  # Первая в верхний регистр
# print(s_3)        # Stroka texta
# print(s)          # sTroka texta


# path = 'C:/Users/PyHS/Desktops/s.py'
# path_1 = path.replace('/', '\\')      # Замена
# print(path_1)  # C:\Users\PyHS\Desktops\s.py

# r = path_1.split('\\') # Разбить по разделителю
# print(r)  # ['C:', 'Users', 'PyHS', 'Desktops', 's.py']
# print(r[-1])  # s.py

# q = open('text.txt', encoding='utf-8')
# print(q.read()) # У нас есть текст,который нужно
                  #  обработать.Убрать все (скобки),"кавычки",
                  # и знаки переноса строки.


# with open("text.txt", encoding="utf-8") as f:
#     text = f.read()

# list_znk = ["(", ")", '"', "\n"]
# for znk in list_znk:
#     text = text.replace(znk, " ")

# print(text)  # У нас есть текст,который нужно  обработать.Убрать все  скобки , кавычки , и знаки переноса строки.
# t = text.split()
# print(t) # ['У', 'нас', 'есть', 'текст,который', 'нужно', 'обработать.Убрать', 
# # 'все', 'скобки', ',', 'кавычки', ',', 'и', 'знаки', 'переноса', 'строки.']


# text = 'У нас есть текст,который нужно обработать.Убрать все (скобки),"кавычки", и знаки переноса строки.'

# filtered_text = ''.join(c for c in text if c not in '()"\n')
# print(filtered_text) # У нас есть текст,который нужно обработать.Убрать все скобки,кавычки, и знаки переноса строки.


# with open("text.txt", encoding="utf-8") as f:
#     text = f.read()

# list_znk = ["(", ")", '"', "\n"]
# for znk in list_znk:
#     text = text.replace(znk, " ")

# print(text)  # У нас есть текст,который нужно  обработать.Убрать все  скобки , кавычки , и знаки переноса строки.
# t = text.split()
# print(t)  # ['У', 'нас', 'есть', 'текст,который', 'нужно', 'обработать.Убрать', 'все', 'скобки', ',', 
#           # 'кавычки', ',', 'и', 'знаки', 'переноса', 'строки.']

# new_text = ' '.join(t)
# print(new_text) # У нас есть текст,который нужно обработать.Убрать все скобки , кавычки , и знаки переноса строки.


with open("text.txt", encoding="utf-8") as f:
    text = f.read()

list_znk = ["(", ")", '"', "\n"]
for znk in list_znk:
    text = text.replace(znk, " ")

print(text)  # У нас есть текст,который нужно  обработать.Убрать все  скобки , кавычки , и знаки переноса строки.
t = text.split()
print(t)  # ['У', 'нас', 'есть', 'текст,который', 'нужно', 'обработать.Убрать', 'все', 'скобки', ',', 
          # 'кавычки', ',', 'и', 'знаки', 'переноса', 'строки.']

new_text = '_*_'.join(t)
print(new_text) # У_*_нас_*_есть_*_текст,который_*_нужно_*_обработать.
                # Убрать_*_все_*_скобки_*_,_*_кавычки_*_,_*_и_*_знаки_*_переноса_*_строки.