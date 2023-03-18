# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

number_from_user = int(input("Введите целое положительное число: "))
if number_from_user > 0:
    first_number = number_from_user
    while first_number // 10 > 0:
        first_number = first_number // 10
    second_number = first_number + number_from_user * 10
    third_number = first_number + second_number * 10
    summation_result = number_from_user + second_number + third_number
    print(f"Сумма чисел {number_from_user}, {second_number} и {third_number} = {summation_result}")
else:
   print("Введенное число не является целым положительным.")