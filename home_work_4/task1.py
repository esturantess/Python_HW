# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def populating_the_list(current_list, required_length, input_description):
    while len(current_list) < required_length:
        next_element = int(input(input_description))
        current_list.append(next_element)
    new_multitude = set(current_list)
    return new_multitude


try:
    multitude_length_1 = int(input("Введите количество элементов первого множества: "))
    multitude_length_2 = int(input("Введите количество элементов второго множества: "))

except ValueError:
    print("Некорректное значение.")
else:
    user_nums_1 = []
    user_nums_2 = []
    input_description_1 = "Введите элемент первого множества: "
    input_description_2 = "Введите элемент второго множества: "
    list_1 = list(populating_the_list(user_nums_1, multitude_length_1, input_description_1))
    list_2 = list(populating_the_list(user_nums_2, multitude_length_2, input_description_2))
    list_3 = []

    if len(list_1) >= len(list_2):
        for el in list_1:
            if el in list_2:
                list_3.append(el)
    else:
        for el in list_2:
            if el in list_1:
                list_3.append(el)
    list_3.sort()
    print("Элементы, встречающиеся в обоих наборах: ", list_3)
