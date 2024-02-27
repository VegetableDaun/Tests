class Cup:
    __slots__ = ('bottom', 'wall')

    def __init__(self, bottom, wall):
        self.bottom = bottom
        self.wall = wall


class Big_Cup(Cup):
    pass


m = Big_Cup(1, 3)
m.L = 3

print(m.bottom, m.wall)
print(m.__dict__)

m = Big_Cup()
print(m.size)
