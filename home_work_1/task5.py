# ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
#
# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

three_digit_number = input("Введите трехзначное число: ")
if len(three_digit_number) == 3:
    print(f"Сумма цифр числа {three_digit_number} = {int(three_digit_number[0]) + int(three_digit_number[1]) + int(three_digit_number[2])}")
else:
    print("Введено некорректное число.")