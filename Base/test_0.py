import math


class Circle:
    __local_1 = 2
    local_2 = 3

    def __new__(cls, *args, **kwargs):
        print('Создание объекта')
        return super().__new__(cls)

    def __init__(self, radius):
        self.radius = radius

    def __del__(self):
        print('Объект', self, 'уничтожен')

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimetre(self):
        return 2 * math.pi * self.radius

    @classmethod
    def A(cls, a, b):
        return cls.__local_1 * cls.local_2 * a / b

    @staticmethod
    def B(a, b):
        return a * b

    def setter(self, a, b):
        self.__local_1 = a
        self.__local_2 = b

    def getter_local(self):
        return self.__local_1, self.__local_2

    def check(self):
        return self.__local_1 * self.__local_2

    def __setattr__(self, key, value):
        if key == 'r':
            print('Данная переменная запрещена к созданию')
        else:
            return super().__setattr__(key, value)

    def __delattr__(self, item):
        print('Удаление переменной')
        return super().__delattr__(item)

    def __getattr__(self, item):
        print('Данного атрибута нет', item)

    def __getattribute__(self, item):
        if item == 'n':
            print(item, 'нельзя извлекать')
        else:
            return super().__getattribute__(item)


class copy_Circle(Circle):
    def __setattr__(self, key, value):
        return super().__setattr__(key, value)


cir_1 = Circle(100)
cir_1.d = 1

cir_2 = copy_Circle(10)
print(cir_2.area())