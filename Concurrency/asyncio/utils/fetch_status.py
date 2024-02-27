from aiohttp import ClientSession

# from Concurrency.asyncio.utils.async_timed import async_timed
from Concurrency.asyncio.utils.delay_functions import delay


# @async_timed()
async def fetch_status(session: ClientSession, url: str, i=0) -> int:
    if i != 0:
        await delay(i)

    async with session.get(url) as result:
        return result.status
