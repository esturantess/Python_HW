# 4) Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.

# Написать скрипт, автоматизирующий его заполнение данными. Для этого:

# a) Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;

# b) Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": f"{item}",
        "quantity": f"{quantity}",
        "price": f"{price}",
        "buyer": f"{buyer}",
        "date": f"{date}"
    }

    with open('orders.json', encoding='utf-8') as f_n:
        objs = json.load(f_n)
        new_list = objs.get('orders')
        new_list.append(dict_to_json)
        objs["orders"] = new_list

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(objs, f_n, indent=4, ensure_ascii=False)


write_order_to_json("Кофемашина с турбопродувом", 1, 10567999, "Зачемов.Н.З", "23.04.2023")
