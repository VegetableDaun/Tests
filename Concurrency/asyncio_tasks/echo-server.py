import asyncio
import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()

    return server_socket

async def listen_for(server_socket, loop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        print(f'Установлено соеденение с {address}')
        asyncio.create_task(send_message(connection, loop))

async def send_message(client_socket, loop):
    while True:
        request = await loop.sock_recv(client_socket, 4096)

        if not request:
            break
        else:
            response = request
            await loop.sock_sendall(client_socket, response)

    print("CLIENT SOCKET was closed")
    client_socket.close()


async def main():
    loop = asyncio.get_event_loop()
    await listen_for(server(), loop)



if __name__ == "__main__":
    asyncio.run(main())
