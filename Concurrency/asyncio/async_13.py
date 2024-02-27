import asyncio
from asyncio import Future


# F.set_result(100)
# F.set_exception(asyncio.exceptions.TimeoutError)

# print(f'Значение хранящиеся в коробке? {F.result()}')

async def main():
    F = Future()
    print(f'Объект Future готов к чтению? {F.done()}')

    res = await F
    return res

asyncio.run(main())




