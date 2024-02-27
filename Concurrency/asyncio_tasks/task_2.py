import asyncio
from time import time

async def new_print(name, sec):
    await asyncio.sleep(sec)
    print(name)

async def main():
    t0 = time()
    tasks = [asyncio.create_task(new_print(f'Function {i}', i)) for i in range(1, 11)]
    await asyncio.gather(*tasks)

    print(f"{time() - t0} секунд выполнялась программа")


asyncio.run(main())