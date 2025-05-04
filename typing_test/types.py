from typing import Any


class User():
    pass


class ProUser(User):
    pass


class TeamUser(User):
    pass


def get_user[T](x: type[T]) -> None:
    pass


a = get_user(ProUser)
