import asyncio
from asyncio import AbstractEventLoop
from multiprocessing import Pool, Process
from functools import partial
from concurrent.futures import ProcessPoolExecutor
def count(count_to: int) -> int:
    counter = 0

    while counter < count_to:
        counter = counter + 1
    return counter

async def main():

    with ProcessPoolExecutor() as process_poll:
        loop: AbstractEventLoop = asyncio.get_event_loop()
        numbers = [300000000, 200000000, 100000000]

        partial_calls: list[partial[int]] = [partial(count, number) for number in numbers]

        calls = []
        for partial_call in partial_calls:
            calls.append(loop.run_in_executor(process_poll, partial_call))

        results = await asyncio.gather(*calls)
        print(results)


if __name__ == '__main__':
    # Process_1 = Process(target=count, args=(100000000,))
    # Process_2 = Process(target=count, args=(200000000,))
    #
    # Process_1.start()
    # Process_2.start()
    #
    # print("Идёт выполнение 1 и 2 процесса")
    # Process_1.join()
    # print("Идёт выполнение 2 процесса")
    # Process_2.join()
    # print("Всё выполнено")

    # with Pool() as process_pool:
    #     pr1 = process_pool.apply_async(count, args=(100000000,))
    #     pr2 = process_pool.apply_async(count, args=(200000000,))
    #
    #     print(pr1.get())
    #     print(pr2.get())

    # with ProcessPoolExecutor() as process_pool:
    #     for result in process_pool.map(count, [100000000, 200000000, 300000000]):
    #         print(result)

    asyncio.run(main=main())