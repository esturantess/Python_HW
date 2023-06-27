class NotNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Число не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    mass = 25
    meters_number = 0.05
    _length = NotNegative()
    _width = NotNegative()

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


Road1 = Road(-20, -5000)
Road1.calculation_of_asphalt_mass()