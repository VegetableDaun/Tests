class Clock:
    def __init__(self, seconds):
        self.seconds = seconds

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Не тот тип данных, нужен int или Cloak")

        sc = other
        if not isinstance(sc, int):
            sc = other.seconds

        return self.seconds == sc

    def __hash__(self):
        return hash((self.seconds,))


c1 = Clock(1000)
c2 = Clock(1000)

print(hash(c1))
print(hash(c2))

d = {c1: 1, c2: 2, 1000: 3}
print(d)
