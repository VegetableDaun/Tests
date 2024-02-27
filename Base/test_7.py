class M:
    def __init__(self):
        self.LUP_0 = 2 ** 3

    @property
    def LUP(self):
        return self.LUP_0


setattr(M, 'foo', 'hello')
print(M.foo)
