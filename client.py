import socket

def request_file(host='localhost', port=12345, filename='example.txt'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))


    client_socket.send(filename.encode())

    response = client_socket.recv(1024).decode()
    if response == "File not found":
        print("File not found on the server.")
        client_socket.close()
        return

    filesize = int(response)
    print(f"Receiving file: {filename} ({filesize} bytes)")

    with open(f"received_{filename}", 'wb') as file:
        remaining = filesize
        while remaining > 0:
            data = client_socket.recv(min(1024, remaining))
            file.write(data)
            remaining -= len(data)

    print(f"File received: received_{filename}")
    client_socket.close()

if __name__ == "__main__":
    request_file()
