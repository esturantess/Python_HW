"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def convert_to_bytes(user_list):
    rus_letters = (
        "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
        "х",
        "ц", "ч", "ш", "щ", "ь",
        "ы", "ъ", "э", "ю", "я")

    if len(user_list) > 0:
        try:
            for el in user_list:
                print(el, " -> ", end="")
                for i in range(len(el)):
                    if el[i] in rus_letters:
                        raise SyntaxError
                print(f"b'{el}'")
        except SyntaxError:
            print("Ошибка! Невозможно сделать запись в байтовом типе.")
            new_list = []
            for i in range(user_list.index(el) + 1, len(user_list)):
                new_list.append(user_list[i])
            convert_to_bytes(new_list)


word_list = ["attribute", "класс", "функция", "type"]
convert_to_bytes(word_list)

# Другой способ

# word_list = ['attribute', 'класс', 'функция', 'type']
#
#
# def convert_to_bytes(user_list):
#     for element in user_list:
#         try:
#             print(eval(f"b'{element}'"))
#         except SyntaxError:
#             print("Ошибка! Невозможно сделать запись в байтовом типе.")
#
#
# convert_to_bytes(word_list)