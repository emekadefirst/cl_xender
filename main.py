from sender import server
from recipient import listener

print("What action do you want to perform?")
response = input("Enter your choice (send/receive): ")

server() if response == "send" else listener() if response == "receive" else print("Invalid request")