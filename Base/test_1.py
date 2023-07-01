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

pt = Point3D(1, 2, 3)
pt.x = 6
pt.y = 6
pt.z = 6
print(pt.x, pt.y, pt.z)