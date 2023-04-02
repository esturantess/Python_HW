# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

from sys import setrecursionlimit

setrecursionlimit(1000000)


class NegativeNumber(Exception):
    pass


def numbers_sum(first_number, second_number, num_sum=0):
    if first_number == 0 and second_number == 0:
        return num_sum
    if first_number > 0:
        first_number -= 1
    elif second_number > 0:
        second_number -= 1
    num_sum += 1
    return numbers_sum(first_number, second_number, num_sum)


try:
    first_user_number = int(input("Введите первое целое неотрицательное число: "))
    if first_user_number < 0:
        raise NegativeNumber()
    second_user_number = int(input("Введите второе целое неотрицательное число: "))
    if second_user_number < 0:
        raise NegativeNumber()

except ValueError:
    print("Некорректное значение.")
except NegativeNumber:
    print("Вы ввели отрицательное число.")

else:
    print(f"Сумма чисел {first_user_number} и {second_user_number} = {numbers_sum(first_user_number, second_user_number)}")
