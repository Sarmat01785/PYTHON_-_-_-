# f-строка, форматирование строк
# %s, .format, f - строка

# enter= input('Your name: ')

# s = 'Hello %s' % enter

# print(s)


# enter = input("Your name: ")

# s = "Hello %s I am %s" % (enter, "Python")

# print(s)

# enter = input("Your name: ")
# s = "Hello {} I am {}".format(enter, "Python")
# print(s)


# enter = input("Your name: ")
# s = "Hello {1} I am {0}".format(enter, "Python")
# print(s)

# enter = input("Your name: ") # Alex
# s = f"Hello {enter}, I can do it in f-string {2 + 2}"
# print(s) # Hello Alex, I can do it in f-string 4


enter = input("Your name: ") # Alex
var = 'stroka'
s = f"Hello {enter}, I can do it in f-string {len(var)}"
print(s) # Hello Alex, I can do it in f-string 6