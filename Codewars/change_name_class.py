class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"


class MyClass(ReNameAbleClass):
    pass


myObject = MyClass()

myObject.change_class_name('LOL')
print(myObject)
