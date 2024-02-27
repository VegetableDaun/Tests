import asyncio
import aiohttp

from time import time

async def main():
    t0 = time()
    fetchs = [asyncio.wait_for(asyncio.create_task(get_inf("http://joyreactor.cc/")), 1),
              asyncio.create_task(get_inf("https://booklover.by/"))]

    text = await asyncio.gather(*fetchs, return_exceptions=True)

    print("Data from", "http://joyreactor.cc/", len(text[0]), "bytes")
    print("Data from", "https://booklover.by/", len(text[1]), "bytes")

    print(f"{time() - t0} секунд выполнялась программа")

async def get_inf(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as result:
            await asyncio.sleep(2)
            return await result.text()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())