import asyncio
import aiohttp

async def main():
    fetchs = [asyncio.create_task(get_inf("http://joyreactor.cc/")),
                  asyncio.create_task(get_inf("https://www.onliner.by/"))]

    text = await asyncio.gather(*fetchs)

    print("Data from", "http://joyreactor.cc/", len(text[0]), "bytes")
    print("Data from", "https://www.onliner.by/", len(text[1]), "bytes")

async def get_inf(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as result:
            return await result.text()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())