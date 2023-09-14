import json
from functools import wraps


def jsonattr(filepath):
    def outer(new_class):
        with open(filepath, 'r') as file:
            unpack = json.load(file)
        for key, value in unpack.items():
            setattr(new_class, key, value)

        @wraps(new_class)
        def wrapper(*args, **kwargs):
            return new_class(*args, **kwargs)

        return wrapper

    return outer


@jsonattr('duplicate.json')
class MyClass:
    def __init__(self, foo, an_int, this_kata_is_awesome):
        self.foo = foo
        self.an_int = an_int
        self.this_kata_is_awesome = this_kata_is_awesome


instance = MyClass("pain", 2, None)

print(instance.foo)
print(MyClass.foo)
