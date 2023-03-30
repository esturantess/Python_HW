# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!

class NegativeNumber(Exception):
    pass


def elements_sum(user_number, first_number, el_sum, iteration_number):
    if user_number == 0:
        return 0
    if user_number == 1:
        return first_number
    elif iteration_number == user_number:
        return el_sum
    elif iteration_number % 2 != 0:
        el_sum -= first_number / 2
    else:
        el_sum += first_number / 2
    return elements_sum(user_number, first_number / 2, el_sum, iteration_number + 1)


try:
    user_num = int(input("Введите количество элементов: "))
    if user_num < 0:
        raise NegativeNumber()
except ValueError:
    print("Вы ввели строку вместо числа.")
except NegativeNumber:
    print("Ошибка: количество элементов не может быть отрицательным.")
else:
    print(f"Количество элементов: {user_num}. Их сумма: {elements_sum(user_num, 1, 1, 1)}")
