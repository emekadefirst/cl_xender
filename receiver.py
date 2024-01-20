import os
import socket
import tqdm

def receive_file(server_ip, server_port, save_path="/storage/emulated/0/downloads/"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Use IPv4
    server.bind((server_ip, server_port))
    server.listen()

    client, addr = server.accept()

    try:
        # Verify file transfer signal
        file_name_signal = client.recv(1024).decode()
        if file_name_signal == "start_file_transfer":
            file_name = client.recv(1024).decode()
            print("Received file name:", file_name)
        else:
            raise ValueError("Invalid file transfer signal")

        # Receive file size
        file_size_bytes = client.recv(8)
        file_size = int.from_bytes(file_size_bytes, byteorder='big')
        print("File size:", file_size, "bytes")

        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, file_name)

        with open(file_path, "wb") as file:
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

        print("File transfer complete.")

    except Exception as e:
        print(f"Error during file transfer: {e}")

    finally:
        client.close()
        server.close()
        
