import asyncio
import logging
import signal
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
                                   max_size=3) as pool:
        while True:
            connection, address = await loop.sock_accept(server_socket)
            connection.setblocking(False)

            print(f"Получен запрос на подключение от {address}")

            asyncio.create_task(request_client(connection, pool, loop))


async def sending_data_client(request: str, pool: asyncpg.pool.Pool, loop: AbstractEventLoop,
                              connection_socket: socket):
    async with pool.acquire() as connection:
        async with connection.transaction():
            task_cursor = connection.cursor(request, prefetch=100)

            async for first_name, last_name, dep in task_cursor:
                await loop.sock_sendall(connection_socket, f'{first_name} {last_name}___{dep}\n'.encode())


async def request_client(connection_socket: socket, pool: asyncpg.Pool, loop: AbstractEventLoop):
    try:
        while data := await loop.sock_recv(connection_socket, 1024):

            if data.decode().split()[0] == 'SELECT_EMP':
                request = SELECT_EMPLOYEES_DEP.format(data.decode().split()[1])

                await sending_data_client(request, pool, loop, connection_socket)

            else:
                await loop.sock_sendall(connection_socket, f'ALL IS OKAY\n'.encode())

    except Exception as ex:
        logging.exception(ex)
    finally:
        connection_socket.close()


async def main():
    server_socket = server()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
