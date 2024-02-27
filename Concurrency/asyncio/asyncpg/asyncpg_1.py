import asyncpg
import asyncio

from SQL_command import *

async def connect():
    connection = await asyncpg.connect(host='localhost',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='')
    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')

    return connection

async def main():
    connection = await connect()

    statements = [CREATE_BRAND_TABLE,
                  CREATE_PRODUCT_TABLE,
                  CREATE_PRODUCT_COLOR_TABLE,
                  CREATE_PRODUCT_SIZE_TABLE,
                  CREATE_SKU_TABLE,
                  SIZE_INSERT,
                  COLOR_INSERT]

    print('Создается база данных product...')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)

    print('База данных product создана!')


    await connection.close()

asyncio.run(main())