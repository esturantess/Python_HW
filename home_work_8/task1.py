# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


def user_input(user_data, user_str=(input("Введите следующую строку: "))):
    if len(user_str) == 0:
        return None
    else:
        user_data.write(user_str + '\n')
        next_str = input("Введите следующую строку: ")
        user_input(user_data, next_str)


user_data = open("user_data.txt", 'w')
user_input(user_data)
