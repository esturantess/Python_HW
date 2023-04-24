# 3)	Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt,
# info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

# a) Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо
# с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

# b) Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;

# c) Проверить работу программы через вызов функции write_to_csv().

import csv
import re


def get_data():
    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
    os_name = re.compile(r'Название ОС:\s*\S*')
    os_code = re.compile(r'Код продукта:\s*\S*')
    os_type = re.compile(r'Тип системы:\s*\S*')
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]
    try:
        file_number = int(input("Введите количество файлов: "))
        for i in range(file_number):
            os_prod_list = []
            os_name_list = []
            os_code_list = []
            os_type_list = []
            file_name = input("Введите навание следующего файла (с расширением): ")
            current_file = open(f"{file_name}")
            for line in current_file:
                if "Изготовитель системы:" in line:
                    os_prod_list.append(os_prod_reg.findall(line)[0].split()[2])
                if "Название ОС:" in line:
                    os_name_list.append(os_name.findall(line)[0].split()[2])
                if "Код продукта:" in line:
                    os_code_list.append(os_code.findall(line)[0].split()[2])
                if "Тип системы:" in line:
                    os_type_list.append(os_type.findall(line)[0].split()[2])
            main_data.append(os_prod_list + os_name_list + os_code_list + os_type_list)
            print(main_data)
            current_file.close()
        return main_data

    except ValueError:
        print("Вы ввели строку вместо числа.")


def write_to_csv(csv_link):
    with open(f'{csv_link}', 'w') as current_csv:
        writer = csv.writer(current_csv, delimiter=';')
        for row in get_data():
            writer.writerow(row)
    with open(f'{csv_link}') as current_csv:
        print(current_csv.read())


write_to_csv("new_file.csv")
