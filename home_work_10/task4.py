"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def convert_to_bytes(user_list):
    bytes_list = []
    for i in range(len(user_list)):
        bytes_list.append(user_list[i].encode('utf-8'))
    return bytes_list


def convert_from_bytes(user_list):
    str_list = []
    for i in range(len(user_list)):
        str_list.append(user_list[i].decode('utf-8'))
    return str_list


word_list = ["разработка", "администрирование", "protocol", "standard"]

print("Байтовое представление слов: ", convert_to_bytes(word_list), sep='\n')
print("Строковое представление слов: ", convert_from_bytes(convert_to_bytes(word_list)), sep='\n')
