import asyncio

import aiohttp

from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        pending = [asyncio.create_task(fetch_status(session, 'https://example.com', 4)),
                   asyncio.create_task(fetch_status(session, 'https://example.com', 3)),
                   asyncio.create_task(fetch_status(session, 'https://example.com', 2)),
                   asyncio.create_task(fetch_status(session, 'https://example.com', 1))]

        while pending:
            done, pending = await asyncio.wait(pending, timeout=1)

            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for done_task in done:
                print(await done_task)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
