from collections.abc import Generator, AsyncGenerator, Coroutine, Iterator, AsyncIterator


async def increment():
    pass


def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'


def infinite_stream(start: int) -> Generator[int]:
    while True:
        yield start
        start += 1


def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1


def infinite_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1


async def infinite_stream(start: int) -> AsyncGenerator[int]:
    while True:
        yield start
        start = await increment(start)


async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
    while True:
        yield start
        start = await increment(start)


async def infinite_stream(start: int) -> AsyncIterator[int]:
    while True:
        yield start
        start = await increment(start)


c: Coroutine[list[str], str, int]  # Some coroutine defined elsewhere
x = c.send('hi')  # Inferred type of 'x' is list[str]


async def bar() -> None:
    y = await c


# async def test():
#     # stm = yield
#     # yield list(stm)
#     s = await
#     return 34
#
#
# gen: Coroutine[list[str], str, int] = test()
# # print(next(gen))
# print(gen.send('dsds'))
#
# # y: Coroutine[list[str], str, int] = test
