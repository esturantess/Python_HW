# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def user_input(input_description, input_type):
    try:
        user_number = input_type(input(input_description))
    except ValueError:
        print("Некорректное значение.")
    else:
        return user_number


def fill_the_list(list_size, input_type):
    new_list = []
    [new_list.append(user_input("Введите элемент списка: ", input_type)) for i in range(list_size)]
    return new_list


def checking_range_membership(new_list, min_value, max_value):
    index_list = []
    count = 0
    for i in range(len(new_list)):
        if max_value >= new_list[i] >= min_value:
            index_list.append(i)
            count += 1
    if count == 0:
        print("Элементов, входящих в заданный диапазон, нет.")
        return 0
    else:
        return index_list


user_list = fill_the_list(user_input("Введите длину списка: ", int), int)
user_min_value = user_input("Введите минимальное значение диапазона: ", int)
user_max_value = user_input("Введите максимальное значение диапазона: ", int)
print("Заданный диапазон: [" + str(user_min_value) + "," + str(user_max_value) + "]")

if checking_range_membership(user_list, user_min_value, user_max_value) != 0:
    print("Индексы элементов, входящих в заданный диапазон: ",
          checking_range_membership(user_list, user_min_value, user_max_value))
