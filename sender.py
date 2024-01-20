import os
import socket

def server(server_ip, server_port):
    print(server_port)
    # Get the list of files in the current directory
    files = [file for file in os.listdir() if os.path.isfile(file)]

    # Filter for video files (you can customize this filter based on your needs)
    video_files = [video for video in files if video.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    # Check if there are any video files in the directory
    if not video_files:
        print("No video files found in the current directory.")
        return

    file_name = video_files[0]
    file_path = os.path.abspath(file_name)
    file_size = os.path.getsize(file_path)

    # Create a socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client.connect((server_ip, server_port))

        # Send file transfer details
        client.sendall(b"start_file_transfer")
        client.sendall(str(file_size).encode())
        client.sendall(file_name.encode())

        # Open and send the file in chunks
        with open(file_path, "rb") as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client.sendall(data)

        # Signal the end of file transfer
        client.sendall(b"<END>")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the file and the socket
        client.close()