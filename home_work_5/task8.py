# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation(user_number, degree, result=1):
    if degree == 0:
        return result
    else:
        result = user_number * exponentiation(user_number, degree - 1, result)
        return result


try:
    user_number = float(input("Введите число: "))
    user_degree = int(input("Введите целую степень: "))
except ValueError:
    print("Некорректное значение.")
else:
    print(f"{user_number} в степени {user_degree} = {exponentiation(user_number, user_degree)}")
