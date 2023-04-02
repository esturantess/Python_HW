# Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число: 123
# Количество четных и нечетных цифр в числе равно: (1, 2)

class NewEx(Exception):
    pass


def counting_even_and_odd_numbers(user_number, even_num_count, odd_num_count):
    if user_number == 0:
        count_result = (even_num_count, odd_num_count)
        return count_result
    elif (user_number % 10) % 2 == 0:
        even_num_count += 1
    else:
        odd_num_count += 1
    return counting_even_and_odd_numbers(user_number // 10, even_num_count, odd_num_count)


try:
    user_num = int(input("Введите натуральное число: "))
    if user_num <= 0:
        raise NewEx()
except ValueError:
    print("Вы ввели строку вместо числа.")
except NewEx:
    print("Вы ввели не натуральное число.")

else:
    print(f"Количество четных и нечетных цифр в числе равно: {counting_even_and_odd_numbers(user_num, 0, 0)}")
