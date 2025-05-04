from typing import NewType

UserId = NewType('UserId', int)

a: UserId = UserId(10)
b: int = 10

def get_user(a: UserId) -> str:
    return str(a * 10)

print(type(a))
print(type(b))
print(a is b)

print(get_user(a))