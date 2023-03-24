# 3. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Далее необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }

class NegativeNumbersEx(Exception):
    pass


class RepeatingItemNumberEx(Exception):
    pass


item_list = []
item_number_list = []
item_name_list = []
item_price_list = []
item_quantity_list = []
item_unit_list = []

while True:
    try:
        item_number = int(input("Введите номер товара: "))
        item_name = input("Введите название товара: ")
        item_price = float(input("Введите цену товара: "))
        item_quantity = int(input("Введите количество товара: "))
        item_unit = input("Введите единицы измерения: ")

        if item_number < 0 or item_price < 0 or item_quantity < 0:
            raise NegativeNumbersEx()
        if item_number in item_number_list:
            raise RepeatingItemNumberEx
        if item_name not in item_name_list:
            item_name_list.append(item_name)
        if item_price not in item_price_list:
            item_price_list.append(item_price)
        if item_quantity not in item_quantity_list:
            item_quantity_list.append(item_quantity)
        if item_unit not in item_unit_list:
            item_unit_list.append(item_unit)

        item_number_list.append(item_number)

    except ValueError:
        print("Некорректное значение.")
    except NegativeNumbersEx:
        print("Ошибка: Номер товара, количество товаров и цена товара не могут быть отрицательными.")
    except RepeatingItemNumberEx:
        print("Номер товара должен быть уникальным.")
    else:
        item_dict = {"Название": item_name, "цена": item_price, "количество": item_quantity, "ед": item_unit}
        item_tuple = (item_number, item_dict)
        item_list.append(item_tuple)
        print(f"Список кортежей: {item_list}")
        analytics_dict = {"Названия": item_name_list, "Цены": item_price_list, "Количества" : item_quantity_list, "Ед" : item_unit_list}
        print(f"Аналитика: {analytics_dict}")
