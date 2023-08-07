class R:
    def WHAT(self):
        self.AAA = 1


class A:
    pass


class B:
    pass


class C(R):
    pass


class D(A, B, C):
    pass


class E(D):
    pass


test = E()
print(E.__mro__)

test.__W = 1
print(test.__dict__)
print(test.__W)
print(test.__sizeof__())
