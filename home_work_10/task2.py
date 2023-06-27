"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def print_type(user_list):
    for i in range(len(user_list)):
        print(f"Тип элемента: ", type(user_list[i]))


def print_content(user_list):
    for i in range(len(user_list)):
        print(f"Содержимое элемента: ", user_list[i])


def print_len(user_list):
    for i in range(len(user_list)):
        print(f"Длина элемента: ", len(user_list[i]))


def print_all(user_list):
    for i in range(len(user_list)):
        print(f"Элемент {i + 1}")
        new_list = [user_list[i]]
        print_type(new_list)
        print_content(new_list)
        print_len(new_list)
        print()


bytes_list = [b"class", b"function", b"method"]
print_all(bytes_list)
