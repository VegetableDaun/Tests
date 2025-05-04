import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_num_3():
    num = 1
    while True:
        if num % 3 == 0:
            print(num, "SECOND OUTPUT")
        num += 1
        await asyncio.sleep(0.1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_num_3())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(app())
    # loop.close()
    asyncio.run(main())
