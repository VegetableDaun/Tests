from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')


def first(l: Sequence[T]) -> T:
    return l[0]


def second[V](l: Sequence[V]) -> V:
    return l[0]


a = first([1, 2, 3, 4, 5, 6])
b = second([1, 2, 3, 4, 5, 6])

print(a, b)
