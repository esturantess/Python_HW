# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

class NewEx(Exception):
    pass


new_list = []

try:
    user_length = int(input("Введите количество элементов в массиве: "))
    user_number = float(input("Введите число: "))
    if user_length < 1:
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
    if user_number > new_list[user_length - 1]:
        nearest_item = new_list[user_length - 1]
    else:
        for i in range(user_length - 1):
            if new_list[i + 1] > user_number > new_list[i]:
                if new_list[i + 1] - user_number <= user_number - new_list[i]:
                    nearest_item = new_list[i + 1]
                else:
                    nearest_item = new_list[i]
    print(f"К числу {user_number} самый близкий элемент в массиве - {nearest_item}.")