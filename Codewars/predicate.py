class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @staticmethod
    def check(other):
        if not isinstance(other, predicate):
            other = predicate(other)
            return other
        else:
            return other

    def __and__(self, other):
        other = self.check(other)

        def outer(*args, **kwargs):
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)

        return self.__class__(outer)

    def __rand__(self, other):
        return self & other

    def __or__(self, other):
        other = self.check(other)

        def outer(*args, **kwargs):
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)

        return self.__class__(outer)

    def __ror__(self, other):
        return self | other

    def __invert__(self):
        def outer(*args, **kwargs):
            return not self.func(*args, **kwargs)

        return self.__class__(outer)


@predicate
def is_even(num):
    return num % 2 == 0


@predicate
def is_positive(num):
    return num > 0


print((is_even & is_positive)(4))
print((is_even & is_positive)(3))
print((is_even | is_positive)(3))
print((~is_even & is_positive)(3))

