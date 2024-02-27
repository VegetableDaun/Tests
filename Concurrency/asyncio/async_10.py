import asyncio
from asyncio import CancelledError
from utils import delay


async def message():
    await asyncio.sleep(3)
    while True:
        for i in range(20):
            print("DONER")
        await asyncio.sleep(6)


async def main():
    long_task = asyncio.create_task(delay(2))
    seconds_elapsed = 0
    while not long_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print('Наша задача была снята')


asyncio.run(main())
