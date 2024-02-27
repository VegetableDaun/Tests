import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
# server_address = ('localhost', 8000)
server_socket.bind(server_address)
server_socket.listen()

connections = []

try:
    while True:
        connection, client_address = server_socket.accept()
        print(f'Получен запрос на подключение от {client_address}!')

        connections.append(connection)

        for con in connections:
            message = con.recv(4096).decode()
            print(f'{client_address} отправило сообщение {message}')

            con.send("DONE\n".encode())
finally:
    for con in connections:
        con.close()

    server_socket.close()