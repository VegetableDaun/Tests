url = 'https://loremflickr.com/320/240'

# from time import time
# import requests
#
#
#
# def get_file(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
#
# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#
#
# def app():
#     t0 = time()
#
#     for i in range(10):
#         write_file(get_file(url))
#
#     print(time() - t0)
#
#
# if __name__ == '__main__':
#     app()

############################
import asyncio
import aiohttp
from time import time

def write_img(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_img(data)

async def main():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print(time() - t0)
