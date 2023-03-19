# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# class NewEx(Exception):
#     pass
#
#
# try:
#     coin_number = int(input("Введите количество монеток: "))
#     tails = int(input("Введите количество монеток, лежащих вверх решкой: "))
#     coat_of_arms = coin_number - tails
#     if coin_number < tails:
#         raise NewEx()
#     print(f"Нужно перевернуть {coat_of_arms} монеток(ки).") if tails >= coat_of_arms else print(f"Нужно перевернуть {tails} монеток(ки).")
# except ValueError:
#     print("Введено некорректное значение.")
# except NewEx:
#     print("Количество монеток, лежащих решкой вверх, не может быть больше общего количества монеток.")

# Решение через цикл

n = int(input("Введите количество монеток: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("Какой стороной лежит следующая монетка? (0 - решка, 1 - герб): "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)