# Задание 3.
#
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        """Информация о сотруднике"""
        self.name = name
        self.surname = surname
        self.position = position
        income_dict = {"wage": wage, "bonus": bonus}
        self._income = income_dict


class Position(Worker):

    def get_full_name(self):
        """Получение полного имени сотрудника"""
        print("Полное имя сотрудника: ")
        return self.name + " " + self.surname

    def get_total_income(self):
        """Получение дохода с учетом премии"""
        worker_income = self._income.get("wage") + self._income.get("bonus")
        print("Доход сотрудника с учетом премии: ")
        return worker_income


Position1 = Position("Мурмурлита", "Мурчанская", "Председатель партии МУРССС", 30000, 60000)
print(Position1.position)
print(Position1.get_full_name())
print(Position1.get_total_income())
print()

Position2 = Position("Экземплярус", "Объектников", "Исполнительный директор отдела генерации странных имён", 10, 0)
print(Position2.position)
print(Position2.get_full_name())
print(str(Position2.get_total_income()) + " рублей")
