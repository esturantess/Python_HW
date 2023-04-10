# Задание 1.
#
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:

    def __int__(self, __color):
        """Свойства светофора"""
        self.__color = "purple in crimson speckles"

    def running():
        """Запуск светофора, переключение в режимы"""
        TrafficLight.__color = "red"
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "yellow"
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = "green"
        print(TrafficLight.__color)
        time.sleep(10)


TrafficLight.running()
