# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
class NewEx(Exception):
    pass


class NewEx1(Exception):
    pass


try:
    first_number = int(input("Введите первое натуральное число: "))
    second_number = int(input("Введите второе натуральное число: "))
    if first_number > 1000 or second_number > 1000:
        raise NewEx()
    if first_number < 1 or second_number < 1:
        raise NewEx1()
    numbers_sum = first_number + second_number
    numbers_product = first_number * second_number
    print(f"Сумма чисел: {numbers_sum}, произведение чисел: {numbers_product}")
    x = None
    y = None
    discriminant = numbers_sum ** 2 - 4 * numbers_product
    x = int((numbers_sum - discriminant ** 0.5) / 2)
    y = int((numbers_sum + discriminant ** 0.5) / 2)
    print(f"Загаданные числа: {x} и {y}")

except ValueError:
    print("Введено некорректное значение.")
except NewEx:
    print("Одно или оба введенных числа больше 1000.")
except NewEx1:
    print("Одно или оба введенных числа меньше 1.")
