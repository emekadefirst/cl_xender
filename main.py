from sender import server
from recipient import listener

cl_xender



print("What action do you want to perform?")
print("A. send")
print("B. receive")

response = input("> ")

if response == "send":
    server()
elif response == "receive":  
    listener()  
else:
    print("Invalid request")
