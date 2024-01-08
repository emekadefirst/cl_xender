import os
import socket

def server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 54321))

    file = open("file name", "rb")
    file_size = os.path.getsize("file name")

    client.send("recieve_file".encode())
    client.send(str(file_size).encode())

    data =  file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()