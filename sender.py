import os
import socket

def server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    file = open("The.Greatest.Beer.Run.Ever.2022.720p.WEBRip.x264.AAC-[YTS.MX].mp4", "rb")
    file_size = os.path.getsize("The.Greatest.Beer.Run.Ever.2022.720p.WEBRip.x264.AAC-[YTS.MX].mp4")

    client.send("recieve_file".encode())
    client.send(str(file_size).encode())

    data =  file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()