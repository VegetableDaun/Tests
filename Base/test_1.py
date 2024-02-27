class Integer():
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.definy_int(value)
        return setattr(instance, self.name, value)

    def definy_int(self, item):
        if type(item) != int:
            raise TypeError('НУЖЕН ИНТЕЖЕР!!!')


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, (tuple, Point3D)):
            raise ArithmeticError('Нужне кортеж с тремя числовыми параметрами или объект класса Point3D')

        sc = other
        if isinstance(other, Point3D):
            sc = other.x, other.y, other.z

        return self.__class__(self.x + sc[0], self.y + sc[1], self.z + sc[2])

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __iadd__(self, other):
        return self + other


pt_1 = Point3D(1, 1, 1)
pt_2 = Point3D(2, 4, 8)
pt_1 += pt_2
print(pt_1)
