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

    def __gt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Не тот тип данных, нужен int или Cloak")

        sc = other
        if not isinstance(sc, int):
            sc = other.seconds

        return self.seconds > sc


c1 = Clock(2000)
c2 = Clock(3000)

print(1000 > c1)
