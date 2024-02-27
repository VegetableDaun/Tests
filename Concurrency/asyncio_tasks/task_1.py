import asyncio
from time import time

async def new_print():
    await asyncio.sleep(2)
    print("Python Exercises")

async def main():
    t0 = time()
    tasks = [asyncio.create_task(new_print()) for _ in range(10)]
    await asyncio.gather(*tasks)

    print(f"{time() - t0} секунд выполнялась программа")


asyncio.run(main())