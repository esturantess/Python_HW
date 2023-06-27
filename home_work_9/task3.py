# 2) Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса

class TypedMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class MyClass(metaclass=TypedMeta):

    def method_1(self):
        pass

    def method_2(self):
        print("Небольшая проблема")


obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)
