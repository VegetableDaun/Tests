import asyncio
from time import time

from utils import delay, async_timed


async def cylce():
    t0 = time()
    t_new = 0

    while t_new < 3:
        t_new = time() - t0
        print('one cycle was ended')
        await asyncio.sleep(0)


@async_timed()
async def main():
    tasks = asyncio.gather(cylce(), delay(6), delay(6), delay(6))

    print(await tasks)


asyncio.run(main())
