import asyncio
from utils import delay
async def main():
    delay_task_0 = asyncio.create_task(delay(2))
    delay_task_1 = asyncio.create_task(delay(3))

    # delay_task_1 = asyncio.wait_for(delay(1.5), timeout=1)

    try:
        result = await asyncio.wait_for(delay_task_1, timeout=2)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут __1__ !')
        print(f'Задача была снята? {delay_task_1.cancelled()}')


    try:
        result = await asyncio.wait_for(delay_task_0, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут __0__!')
        print(f'Задача была снята? {delay_task_0.cancelled()}')

asyncio.run(main())