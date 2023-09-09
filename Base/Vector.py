class Vector:
    def __init__(self, vector):
        self.vector = vector
    def __str__(self):
        return f'{self.vector}'
    def __check(self, v):
        if len(self.vector) != len(v):
            raise Exception

    def __add__(self, v):
        self.__check(v)
        new_vector = [i + j for i, j in zip(self.vector, v)]
        return Vector(new_vector)

V_1 = Vector([1, 3, 8])
V_2 = V_1 + [2, 2, 1]
print(V_2)

