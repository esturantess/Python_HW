# Задание 2.
#
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#
# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600

time_sec = int(input("Введите время в секундах: "))
time_min = int(time_sec / 60)
time_hours = int(time_min / 60)
print(f"Время в ч:м:с - {time_hours} : {time_min} : {time_sec}")
