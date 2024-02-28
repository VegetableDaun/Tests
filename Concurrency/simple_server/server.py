import asyncio
import logging
import socket
from asyncio import AbstractEventLoop

import asyncpg

from database import connect_to_database, connect_to_database_pool
from SQL_command import *


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    return server_socket


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    async with asyncpg.create_pool(host='127.0.0.1',
                                   port=5432,
                                   user='postgres',
                                   database='employees',
                                   password='postgres',
                                   min_size=1,
                                   max_size=2) as pool:

        while True:
            connection, address = await loop.sock_accept(server_socket)
            connection.setblocking(False)

            print(f"Получен запрос на подключение от {address}")

            asyncio.create_task(take_command(connection, pool, loop))


async def res_connection_pool(pool: asyncpg.pool.Pool, request: str):
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.cursor(request)

async def take_command(connection_socket: socket, pool: asyncpg.Pool, loop: AbstractEventLoop):
        try:
            while data := await loop.sock_recv(connection_socket, 1024):

                if data.decode().split()[0] == 'SELECT_EMP':
                    request = SELECT_EMPLOYEES_DEP.format(data.decode().split()[1])

                    results = await res_connection_pool(pool, request)

                    # print(results)

                    # async for first_name, last_name, dep in results:
                    #     await loop.sock_sendall(connection_socket, f'{first_name} {last_name}___{dep}\n'.encode())
                    # await loop.sock_sendall(connection_socket, f'ALL IS OKAY, {results} \n'.encode())

                    # async for i in results.fetch(100):
                    #     print(i)
                        # await loop.sock_sendall(connection_socket, f'{first_name} {last_name}___{dep}\n'.encode())

        except Exception as ex:
            logging.exception(ex)
        finally:
            connection_socket.close()


async def main():
    server_socket = server()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
