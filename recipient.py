import socket
import tqdm

def listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()

    client,  addr =server.accept()

    file_name = client.recv(1024).decode()
    print(file_name)
    file_size_bytes = client.recv(8)  # assuming the size can be represented in 8 bytes
    file_size = int.from_bytes(file_size_bytes, byteorder='big')  # convert bytes to integer
    print(file_size)

    file = open(file_name, "wb")

    file_bytes = b""

    done = False

    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=file_size)

    while not done:
        data = client.recv(1024)
        if data[-5:] == b"<END>":
            done = True
            data = data[:-5]  # remove the "<END>" marker from the last chunk
        file_bytes += data
        progress.update(len(data))
        
    file.write(file_bytes)

    file.close()
    client.close()
    server.close()



