import socket
import os

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        filename = client_socket.recv(1024).decode()
        if os.path.exists(filename):
            filesize = os.path.getsize(filename)
            client_socket.send(str(filesize).encode())

            with open(filename, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    client_socket.send(data)
            print(f"File {filename} sent to {address}")
        else:
            client_socket.send(b"File not found")
        client_socket.close()

if __name__ == "__main__":
    start_server()
