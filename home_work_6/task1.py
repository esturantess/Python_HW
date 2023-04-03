# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

class NegativeNumber(Exception):
    pass


def user_input(input_description, input_type):
    try:
        user_number = input_type(input(input_description))
    except ValueError:
        print("Некорректное значение.")
    else:
        return user_number


def fill_array_with_arithmetic_progression(array_size, first_el, progression_diff, new_array=[]):
    for i in range(array_size):
        new_array.append(first_el + i * progression_diff)
    return new_array



try:
    first_element = user_input("Введите первый элемент: ", float)
    progression_difference = user_input("Введите разность прогрессии: ", float)
    elements_number = user_input("Введите количество элементов: ", int)
    if elements_number < 0:
        raise NegativeNumber()
except NegativeNumber:
    print("Ошибка: значение не может быть отрицательным.")
else:
    print(fill_array_with_arithmetic_progression(elements_number, first_element, progression_difference))
