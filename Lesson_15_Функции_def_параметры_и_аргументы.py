# Функции def, параметры и аргументы
def count_elements(items):
    """
    Возвращает количество элементов в переданном списке.

    :param items: Список для подсчета элементов
    :return: количество элементов в списке
    """
    return len(items)


# Пример вызова функции
elements = [9, 8, 7, 6]
print(count_elements(elements))  # Выведет 4


def greet(name="мир"):
    """
    Выводит приветствие.

    :param name: Имя для приветствия, по умолчанию 'мир'
    :return: None
    """
    print(f"Привет, {name}!")


# Пример вызова функции с параметром по умолчанию и без него
greet()  # Выведет "Привет, мир!"
greet("Алексей")  # Выведет "Привет, Алексей!"


def calculate_area(length, width=1):
    """
    Возвращает площадь прямоугольника по заданным длине и ширине.

    :param length: Длина прямоугольника
    :param width: ширина прямоугольника, по умолчанию 1
    :return: площадь прямоугольника
    """
    return length * width


# Пример вызова функции с одним и двумя аргументами
print(calculate_area(5))  # Выведет 5
print(calculate_area(5, 3))  # Выведет 15


def count_list(items, include_type=False, start_count=0):
    """
    Подсчитывает количество элементов в списке и, опционально, возвращает тип первого элемента.

    :param items: Список для подсчета элементов
    :param include_type: флаг, указывающий на необходимость возвращения типа первого элемента
    :param start_count: начальное значение счетчика (используется для начала подсчета с заданного числа)
    :return: количество элементов и, если include_type истина, тип первого элемента
    """
    count = start_count + len(items)
    if include_type and items:
        item_type = type(items[0])
        return count, item_type
    return count


# Примеры использования функции
numbers = [9, 8, 7, 6]
print(count_list(numbers))  # Выводит количество элементов в списке
print(count_list(numbers, True))  # Выводит количество элементов и тип первого элемента
print(count_list(numbers, True, -1))  # Начинает подсчет с -1
