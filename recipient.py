import os
import socket
import tqdm

def listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Use IPv4
    server.bind(("192.168.120.7", 54321))  # Use the correct IP address and port
    server.listen()

    client, addr = server.accept()

    file_name = client.recv(1024).decode()
    print("Receiving file:", file_name)

    file_size_bytes = client.recv(8)
    file_size = int.from_bytes(file_size_bytes, byteorder='big')
    print("File size:", file_size, "bytes")

    save_path = "/storage/emulated/0/downloads/"  # Change this to the correct path on your phone
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, file_name)
    file = open(file_path, "wb")

    done = False

    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=file_size)

    while not done:
        data = client.recv(1024)
        if not data:
            break
        if data[-5:] == b"<END>":
            done = True
            data = data[:-5]
        file.write(data)
        progress.update(len(data))

    print("Done")

    file.close()
    client.close()
    server.close()

