# Задание 2.
#
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    mass = 25
    meters_number = 0.05

    def __init__(self, length, width):
        """Свойства дороги"""
        self._length = length
        self._width = width
        self.thickness = 1

    def calculation_of_asphalt_mass(self):
        """Расчет массы асфальта"""
        calc_result = self._length * self._width * self.mass * self.meters_number
        print("Результат в кг: ", calc_result)
        print("Результат в т: ", calc_result / 1000)


Road1 = Road(20, 5000)
Road1.calculation_of_asphalt_mass()

