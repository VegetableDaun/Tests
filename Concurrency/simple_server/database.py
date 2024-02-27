import asyncpg


async def connect_to_database():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='employees',
                                       password='postgres')

    return connection


async def connect_to_database_pool():
    async with asyncpg.create_pool(host='127.0.0.1',
                                   port=5432,
                                   user='postgres',
                                   database='employees',
                                   password='postgres',
                                   min_size=1,
                                   max_size=10) as pool:
        return pool
