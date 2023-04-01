# Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# Пример:
# для n = 5
# 1+2+3+4+5 = 5(5+1)/2
# Нужно написать рекурсивную ф-цию только для левой части выражения!
# Результат нужно сверить с правой частью.
# Правой части выражения в рекурсивной ф-ции быть не должно!
# Решите через рекурсию. В задании нельзя применять циклы.

from sys import setrecursionlimit

setrecursionlimit(1000000)


class NotNaturalNumber(Exception):
    pass


def numbers_sum(last_number, current_number=1, sum=0):
    if current_number > last_number:
        return sum
    else:
        sum += current_number
        current_number += 1
        return numbers_sum(last_number, current_number, sum)


try:
    user_number = int(input("Введите натуральное число: "))
    if user_number < 1:
        raise NotNaturalNumber()
except ValueError:
    print("Некорректное значение.")
except NotNaturalNumber:
    print("Вы ввели не натуральное число.")
else:
    expression_right_side = user_number * (user_number + 1) / 2
    expression_left_side = numbers_sum(user_number)
    if expression_right_side == expression_left_side:
        print(f"Для числа", user_number, "равенство выполняется.")
    else:
        print(f"Для числа", user_number, "равенство не выполняется.")
