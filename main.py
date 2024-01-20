from sender import server
from recipient import listener

print("What action do you want to perform?")
response = input("Enter your choice (send/receive): ")

if response == "send":
    # Get user input for server IP and port
    server_ip = input("Enter server IP: ")
    server_port_num = input("Enter server port: ")

    # Use default port 54321 if the user didn't provide a port
    server_port = 54321 if server_port_num == '' else int(server_port_num)

    # Display the default port message only when the default port is used
    if server_port == 54321:
        print('Using default port: 54321')
    server(server_ip, server_port)
elif response == "receive":
    listener()
else: print("Invalid request")
