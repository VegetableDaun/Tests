import math


class Fraction:

    def __init__(self, numerator, denominator):
        self.top, self.bottom = self.short(numerator, denominator)

    # Equality test

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return self.__class__(new_top, new_bottom)

    def __repr__(self):
        return f'{self.top}/{self.bottom}'

    @staticmethod
    def Factor(n):
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        return Ans

    def short(self, numerator, denominator):
        divider = 1
        Factor_numerator = self.Factor(numerator)
        Factor_denominator = self.Factor(denominator)
        for i in Factor_numerator:
            if i in Factor_denominator:
                divider *= i
                Factor_denominator.remove(i)
        return numerator // divider, denominator // divider


print(Fraction(128234, 82064))
