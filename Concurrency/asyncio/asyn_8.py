import asyncio

from utils import delay


async def add_one(number: int) -> int:
    await delay(5)
    return number + 1


async def hello_world_message() -> str:
    await delay(10)
    return "Hello World!"


async def main() -> None:
    hello_cur = asyncio.create_task(hello_world_message())
    one_plus_cur = asyncio.create_task(add_one(1))

    one_plus_res = await one_plus_cur

    print(one_plus_res)

    message = await hello_cur
    print(message)


asyncio.run(main())
