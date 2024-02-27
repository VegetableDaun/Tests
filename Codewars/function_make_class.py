def make_class(*sargs, **skwargs):
    class class_name:
        __variables = dict.fromkeys(sargs)

        def __init__(self, *args):
            self.__dict__ = self.__variables
            i = 0
            for name in self.__dict__:
                self.__dict__[name] = args[i]
                i += 1

    return class_name


Animel = make_class("name", "species", "age", "health", "weight", "color")

dog1 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")

print(dog1.name, dog1.species, dog1.age, dog1.health, dog1.weight, dog1.color)
