import asyncio
import logging
import socket
from asyncio import AbstractEventLoop

from database import connect_to_database
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
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)

        print(f"Получен запрос на подключение от {address}")
        asyncio.create_task(take_command(connection, loop))


async def take_command(connection_socket: socket, loop: AbstractEventLoop):
    connection_database = await connect_to_database()

    try:
        while data := await loop.sock_recv(connection_socket, 1024):

            if data.decode().split()[0] == 'SELECT_EMP':
                SELECT_EMPLOYEES = SELECT_EMPLOYEES_DEP.format(data.decode().split()[1])

                results = await connection_database.fetch(SELECT_EMPLOYEES)

                for first_name, last_name, dep in results:

                    await loop.sock_sendall(connection_socket, f'{first_name}-{last_name}-{dep}\n'.encode())
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection_database.close()
        connection_socket.close()


async def main():
    server_socket = server()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
