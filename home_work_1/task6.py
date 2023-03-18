# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number_of_cranes = int(input("Введите количество журавликов: "))
if number_of_cranes >= 6 and number_of_cranes % 6 == 0:
    first_kid_cranes = number_of_cranes / 6
    second_kid_cranes = first_kid_cranes
    third_kid_cranes = number_of_cranes - first_kid_cranes * 2
    print(f"Петя сделал {int(first_kid_cranes)} журавлика(ов), Серёжа - {int(second_kid_cranes)}, а Катя - {int(third_kid_cranes)} журавликов.")
else:
    print("Целочисленных решений нет.")