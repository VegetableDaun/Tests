import socket
from select import select

socket_list = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    socket_list.append(client_socket)
    print("Connetion from", addr)

def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "HI {}\n".format(request.decode()).encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        ready_to_read, _, _ = select(socket_list, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == "__main__":
    socket_list.append(server_socket)
    event_loop()