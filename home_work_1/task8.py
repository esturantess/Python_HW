# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_length = int(input("Введите длину шоколадки в дольках: "))
chocolate_width = int(input("Введите ширину шоколадки в дольках: "))
slices_to_broke = int(input("Введите количество долек, которые нужно отломить: "))

if slices_to_broke % chocolate_width == 0 or slices_to_broke % chocolate_length == 0:
    print(f"YES! От шоколадки размером {chocolate_length} на {chocolate_width} можно отломить {slices_to_broke} долек.")
else:
    print(f"NO! От шоколадки размером {chocolate_length} на {chocolate_width} нельзя отломить {slices_to_broke} долек.")