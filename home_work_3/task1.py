# БАЗОВЫЕ ЗАДАНИЯ:
#
# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

class NewEx(Exception):
    pass


try:
    month = int(input("Введите номер месяца: "))
    if month < 1 or month > 12:
        raise NewEx()
except ValueError:
    print("Введено некорректное значение.")
except NewEx:
    print("Месяца с таким номером не существует.")
else:

    seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень',
                    'Зима']
    print(f'Результат через список: {seasons_list[month - 1]}')

    seasons_dict = {1: 'Зима', 2: 'Зима', 12: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето',
                    8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень'}
    print(f'Результат через словарь: {seasons_dict[month]}')