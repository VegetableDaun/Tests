import asyncio

from utils import delay, async_timed


@async_timed()
async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        result = await task
        print(result)


asyncio.run(main())
