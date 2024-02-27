import asyncio
import asyncpg

async def connect_to_database():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='employees',
                                       password='')

    return connection

