from dataclasses import dataclass


class Compute:
    def __init__(self, name, memory_size):
        self.name = name
        self.memory_size = memory_size


class Saver:
    def save(self, other):
        raise Exception('Нужно переопределить метод save')

    def CLOCK(self):
        self.CLOCK = True


class Saver_to_file(Saver):
    def save(self, other):
        print(f'Сохранение класса {other} в файл ')


@dataclass
class Phone:
    name: str
    memory_size: int


P = Phone('apple', 1600)
print(P.__dict__)

c_1 = Compute('apple', 1600)
sv = Saver_to_file()
sv.save(c_1)
