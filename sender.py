import os
import socket

def server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.120.7", 54321))

    file_path = "movtest.mp4"
    file_name = os.path.basename(file_path)

    file = open(file_path, "rb")
    file_size = os.path.getsize(file_path)

    client.send("receive_file".encode())
    client.send(str(file_size).encode())
    client.send(file_name.encode())  # Send the file name as well

    data = file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()
