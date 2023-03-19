# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

try:
    max_number = int(input("Введите число: "))
    temp = 0
    while 2 ** temp <= max_number:
        print(2 ** temp)
        temp += 1
except ValueError:
    print("Введено некорректное значение.")

