# ДОПОЛНИТЕЛЬНЫЕ:
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

class NewEx(Exception):
    pass


new_list = []

try:
    user_length = int(input("Введите количество элементов в массиве: "))
    user_number = int(input("Введите искомый элемент в массиве: "))
    if user_length < 1 or user_number < 1:
        raise NewEx()
except ValueError:
    print("Введено некорректное значение.")
except NewEx:
    print("Ошибка: введено не натуральное число.")
else:
    for i in range(user_length):
        new_list.append(i + 1)
        number_count = new_list.count(user_number)
    print(new_list)
    print(f"Число {user_number} содержится в массиве {number_count} раз.")

