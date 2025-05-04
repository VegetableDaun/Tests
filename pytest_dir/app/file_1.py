class Calculator:
    def divide(self, x: int | float, y: int | float) -> int | float:
        return x / y

    def sum(self, x: int | float, y: int | float) -> int | float:
        if isinstance(x, str):
            raise TypeError()

        if isinstance(y, str):
            raise TypeError()

        return x + y


def square(x: int | float) -> int | float:
    return x * x
