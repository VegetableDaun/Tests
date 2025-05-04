# from typing import Callable, Awaitable
from collections.abc import Callable


def test_0() -> str:
    pass


def test_1():
    pass


a: Callable([], None) = test_0
b: Callable([], None) = test_1


def concat(x: str, y: str) -> str:
    return x + y

x: Callable[[str, str], str]
x = str     # OK
x = concat  # Also OK
