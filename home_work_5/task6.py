# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import random


def guess_the_number(riddled_number, attempt_number):
    if attempt_number == 11:
        print(f"Количество попыток истекло. Загаданное число: ", riddled_number)
    else:
        user_number = int(input("Введите загаданное число: "))
        if user_number == riddled_number:
            print("Вы отгадали число!")
            return None
        elif user_number < riddled_number:
            print(f"Загаданное число больше, чем ", user_number)
        else:
            print(f"Загаданное число меньше, чем ", user_number)
        attempt_number += 1
        guess_the_number(riddled_number, attempt_number)


riddled_number = random.randint(0, 101)
print("Загадано число от 0 до 100. Попробуйте угадать его.")
guess_the_number(riddled_number, 1)
