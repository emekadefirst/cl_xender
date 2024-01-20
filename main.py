from sender import server
from recipient import listener

def get_server_info():
    """Gathers server IP and port information from the user."""

    server_ip = input("Enter server IP: ")
    port_number = input("Enter server port (leave blank for default): ")

    server_port = 54321 if not port_number else int(port_number)

    if server_port == 54321:
        print("Using default port: 54321")

    return server_ip, server_port

def main():
    """Prompts the user for action and calls appropriate functions."""

    print("What action do you want to perform?")
    response = input("Enter your choice (send/receive): ")

    if response == "send":
        server_ip, server_port = get_server_info()
        server(server_ip, server_port)
    elif response == "receive":
        server_ip, server_port = get_server_info()
        save_path = ""
        listener(server_ip, server_port, save_path)
    else: print("Invalid request")

if __name__ == "__main__":
    main()