# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# import random
#
# list_of_bushes = []
# berries_dict = {}
#
# try:
#     number_of_bushes = int(input("Введите количество кустов: "))
#
# except ValueError:
#     print("Некорректное значение.")
#
# else:
#     for i in range(1, number_of_bushes + 1):
#         list_of_bushes.append(i)
#     print("Список кустов: ", list_of_bushes)
#
#     for el in list_of_bushes:
#         berries_number = random.randint(1, 15)
#         berries_dict.update({el: berries_number})
#     print("Сколько ягод на каждом кусте (номер куста: количество ягод): ", berries_dict)
#     berries_list = list(berries_dict.values())
#     print("Список ягод: ", berries_list)
#     max_berries_numbers = 0
#     temp = 0
#     if len(berries_list) == 1:
#         max_berries_numbers = berries_list[0]
#     for i in range(len(berries_list) - 1):
#         if berries_list[i] == 0:
#             continue
#         if berries_list[i] >= berries_list[i - 1]:
#             temp = berries_list[i] + berries_list[i - 1]
#             berries_list[i - 1] = 0
#             if len(berries_list) < 3:
#                 berries_list[i] = 0
#         elif berries_list[i - 1] > berries_list[i]:
#             temp = berries_list[i] + list_of_bushes[i]
#             berries_list[i - 1] -= berries_list[i]
#             if len(berries_list) < 3:
#                 berries_list[i] = 0
#         if berries_list[i] >= berries_list[i + 1]:
#             temp += berries_list[i + 1]
#             berries_list[i + 1] = 0
#             if len(berries_list) < 3:
#                 berries_list[i] = 0
#         elif berries_list[i + 1] > berries_list[i]:
#             temp += berries_list[i]
#             berries_list[i + 1] -= berries_list[i]
#             if len(berries_list) < 3:
#                 berries_list[i] = 0
#         berries_list[i] = 0
#         if temp > max_berries_numbers:
#             max_berries_numbers = temp
#     print("Максимальное количество ягод, которые можно собрать за заход:", max_berries_numbers)

Эталонное решение:

n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i-1] + arr[i] + arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))