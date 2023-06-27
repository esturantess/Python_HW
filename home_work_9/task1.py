class IsStr:

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Некорректные данные!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = IsStr()
    surname = IsStr()

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


Position1 = Position("Геннадий", "Крокодильников", "Крокодитель первой категории", 770000, 77600)
print(Position1.position)
print(Position1.get_full_name())
print(str(Position1.get_total_income()) + " крокобаксов")
print()

Position2 = Position("Атрибутто де ля Связноповеденнио", "Дескрипторро",
                     "Проектный менеджер отдела генерации странных имён", 15, 0)
print(Position2.position)
print(Position2.get_full_name())
print(str(Position2.get_total_income()) + " рублей")

Wrong_Position = Position(1, "Два", "Три", 4, 5)
print(Wrong_Position.position)
print(Wrong_Position.get_full_name())
print(Wrong_Position.get_total_income())

