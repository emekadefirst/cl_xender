import os
import socket

def server():
    print
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.120.7", 54321))

    file_path = "/Users/VICTOR/Desktop/cl_xender/moive.mp4"
    file_name = os.path.basename(file_path)

    file = open(file_path, "rb")
    file_size = os.path.getsize(file_path)

    # sender.py
    client.send("start_file_transfer".encode())
    client.send(str(file_size).encode())
    client.send(file_name.encode())   

    data = file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()
