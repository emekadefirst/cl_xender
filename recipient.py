import socket
import tqdm

def listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 54321))  # Use the custom port
    server.listen()

    client, addr = server.accept()

    file_name = client.recv(1024).decode()
    print(file_name)
    file_size_bytes = client.recv(8)
    file_size = int.from_bytes(file_size_bytes, byteorder='big')
    print(file_size)

    file = open(file_name, "wb")

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

    file.close()
    client.close()
    server.close()
